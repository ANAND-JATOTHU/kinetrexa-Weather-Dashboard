from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import login
from django.contrib import messages
from .models import FavoriteLocation, WeatherSearchLog
from .forms import UserRegisterForm, AddLocationForm, EditLocationForm
from .services.weather_api import WeatherService, WeatherAPIException

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'auth/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            messages.success(request, 'Registration successful. Welcome to the Weather Dashboard!')
            return redirect('dashboard')
        return render(request, 'auth/register.html', {'form': form})

class DashboardView(LoginRequiredMixin, ListView):
    model = FavoriteLocation
    template_name = 'dashboard.html'
    context_object_name = 'locations'

    def get_queryset(self):
        return FavoriteLocation.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        weather_service = WeatherService()
        locations_data = []
        for loc in context['locations']:
            try:
                weather = weather_service.get_current_weather(loc.city_name)
                locations_data.append({'location': loc, 'weather': weather, 'error': None})
            except WeatherAPIException as e:
                locations_data.append({'location': loc, 'weather': None, 'error': str(e)})
        context['locations_data'] = locations_data
        return context

class AddLocationView(LoginRequiredMixin, CreateView):
    model = FavoriteLocation
    form_class = AddLocationForm
    template_name = 'location_form.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        city_name = form.cleaned_data['city_name']
        weather_service = WeatherService()
        
        try:
            # Validate city exists
            weather_service.get_current_weather(city_name)
            
            # Log the search
            WeatherSearchLog.objects.create(
                user=self.request.user,
                query_string=city_name,
                status_code=200
            )
            
            # Ensure it doesn't already exist for this user
            if FavoriteLocation.objects.filter(user=self.request.user, city_name__iexact=city_name).exists():
                messages.error(self.request, f"{city_name} is already in your dashboard.")
                return self.form_invalid(form)

            form.instance.user = self.request.user
            messages.success(self.request, f"{city_name} added successfully.")
            return super().form_valid(form)
            
        except WeatherAPIException as e:
            # Log the failed search
            WeatherSearchLog.objects.create(
                user=self.request.user,
                query_string=city_name,
                status_code=e.status_code or 500
            )
            messages.error(self.request, str(e))
            return self.form_invalid(form)

class CityDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = FavoriteLocation
    template_name = 'location_detail.html'
    context_object_name = 'location'

    def test_func(self):
        return self.get_object().user == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        weather_service = WeatherService()
        try:
            context['current_weather'] = weather_service.get_current_weather(self.object.city_name)
            context['forecast'] = weather_service.get_forecast(self.object.city_name)
        except WeatherAPIException as e:
            messages.error(self.request, str(e))
        return context

class EditLocationView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = FavoriteLocation
    form_class = EditLocationForm
    template_name = 'location_form.html'
    success_url = reverse_lazy('dashboard')

    def test_func(self):
        return self.get_object().user == self.request.user

    def form_valid(self, form):
        messages.success(self.request, "Location nickname updated.")
        return super().form_valid(form)

class DeleteLocationView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = FavoriteLocation
    template_name = 'location_confirm_delete.html'
    success_url = reverse_lazy('dashboard')

    def test_func(self):
        return self.get_object().user == self.request.user

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Location removed from your dashboard.")
        return super().delete(request, *args, **kwargs)

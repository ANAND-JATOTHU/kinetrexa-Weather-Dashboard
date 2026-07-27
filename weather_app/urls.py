from django.urls import path
from . import views

urlpatterns = [
    path('', views.DashboardView.as_view(), name='dashboard'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('location/add/', views.AddLocationView.as_view(), name='add_location'),
    path('location/<int:pk>/', views.CityDetailView.as_view(), name='city_detail'),
    path('location/<int:pk>/edit/', views.EditLocationView.as_view(), name='edit_location'),
    path('location/<int:pk>/delete/', views.DeleteLocationView.as_view(), name='delete_location'),
]

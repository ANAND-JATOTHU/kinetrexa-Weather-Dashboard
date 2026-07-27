from django import forms
from django.contrib.auth.models import User
from .models import FavoriteLocation

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data


class AddLocationForm(forms.ModelForm):
    class Meta:
        model = FavoriteLocation
        fields = ['city_name', 'custom_nickname']
        widgets = {
            'city_name': forms.TextInput(attrs={'placeholder': 'e.g., London, UK'}),
            'custom_nickname': forms.TextInput(attrs={'placeholder': 'e.g., Home (optional)'})
        }

class EditLocationForm(forms.ModelForm):
    class Meta:
        model = FavoriteLocation
        fields = ['custom_nickname']

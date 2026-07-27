from django.db import models
from django.contrib.auth.models import User

class FavoriteLocation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_locations')
    city_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10, blank=True, null=True)
    custom_nickname = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'city_name')
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.custom_nickname or self.city_name} - {self.user.username}"


class WeatherSearchLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='search_logs')
    query_string = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    status_code = models.IntegerField(help_text="HTTP status code from API or internal result code")

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.query_string} at {self.timestamp} ({self.status_code})"

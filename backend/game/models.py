from email.policy import default
from django.db import models
from django.utils import timezone


class PlayedGameBy(models.Model):
    users = models.CharField(max_length = 180)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return self.users

class ThemeAvailable(models.Model):
    theme_id = models.CharField(max_length=20)
    theme_name = models.CharField(max_length=30)
    theme_des = models.TextField(blank=True, null=True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    theme_image = models.ImageField(upload_to='themes/images', null=True)
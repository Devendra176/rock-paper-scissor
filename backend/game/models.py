from django.db import models
from django.utils import timezone
# Create your models here.

class PlayedGameBy(models.Model):
    users = models.CharField(max_length = 180)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['created_at']
    
    def __str__(self):
        return self.users
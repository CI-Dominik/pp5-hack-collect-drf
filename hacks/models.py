from django.db import models
from django.contrib.auth.models import User


class Hack(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='../default_profile_picture_tfoiel.webp',
        blank=False
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'ID: {self.id} - {self.title}, by {self.owner}'

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, blank=True)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/',
        default='../default_profile_picture_tfoiel.webp',
        blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.owner}'s profile"


# Function to create a new profile for a newly registered user

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


# Create profiile for newly created users

post_save.connect(create_profile, sender=User._meta.model)

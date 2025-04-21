from django.db import models
from django.contrib.auth.models import User
from categories.models import Category


class Hack(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=100)
    content = models.TextField(blank=False, max_length=255)
    image = models.ImageField(
        upload_to='images/',
        blank=False
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_DEFAULT,
        null=True,
        default=None
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'ID: {self.id} - {self.title}, by {self.owner}'

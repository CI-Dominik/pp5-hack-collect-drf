from django.db import models
from django.contrib.auth.models import User
from hacks.models import Hack


class Comment(models.Model):
    """
    Comment model for Hacks in the frontend.
    "Owner" relates to the person posting.
    "Hack" relates to the Hack it is posted in.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    hack = models.ForeignKey(
        Hack, related_name='comments', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField(max_length=255)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content

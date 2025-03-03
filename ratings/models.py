from django.db import models
from django.contrib.auth.models import User
from hacks.models import Hack


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hack = models.ForeignKey(Hack, on_delete=models.CASCADE)
    rating = models.IntegerField(
        choices=[
            (1, '1 Star'),
            (2, '2 Stars'),
            (3, '3 Stars'),
            (4, '4 Stars'),
            (5, '5 Stars')
            ]
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'life_hack')

    def __str__(self):
        return f"{self.user.username} gave {self.hack.title} {self.rating}"

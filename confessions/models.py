from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Confession(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.PositiveIntegerField(default=0)  # Likes count

    def __str__(self):
        return f"Confession #{self.id} by {self.user.profile.anonymous_id}"

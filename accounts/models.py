from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    college = models.CharField(max_length=100)
    anonymous_id = models.CharField(max_length=100, unique=True, blank=True, null=True, help_text="A unique anonymous ID for the user.")

    def __str__(self):
        return self.user.username

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

class AppUser(AbstractUser):
    pass

class AppUserSettings(models.Model):
    """Represents the options that a user has configured for their account."""
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE)

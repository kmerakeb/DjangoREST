from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

class CustomUser(AbstractUser):
    # First/last name is not a global-friendly pattern
    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.email
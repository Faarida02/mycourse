from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_email_verified = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)

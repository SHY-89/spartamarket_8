from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Users(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, default="images/default_user.png")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    followings = models.ManyToManyField(
        "self", related_name="followers", symmetrical=False
    )
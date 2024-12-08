from django.db import models
from django.contrib.auth.models import AbstractUser



class CustomUser(AbstractUser):

    email = models.EmailField(unique=True)
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(upload_to='static/images/avatars', null=True, blank=True)

    def __str__(self):
        return self.username

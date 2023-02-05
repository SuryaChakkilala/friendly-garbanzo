from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    designation = models.CharField(max_length=150)
    department = models.CharField(max_length=150)
    organization = models.CharField(max_length=150)
    place = models.CharField(max_length=150)

    def __str__(self):
        return self.username
from django.db import models
from django.contrib.auth.models import User

# Django User model

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    bio = models.CharField(max_length=200, null=True)


class Strategy(models.Model):
    name = models.CharField(max_length=200, null=True)
    isProfitable = models.BooleanField()

from django.db import models

# Create your models here.

# Django User model

class Profile(models.Model):
    bio = models.CharField(max_length=200, null=True)


class Strategy(models.Model):
    name = models.CharField(max_length=200, null=True)
    isProfitable = models.BooleanField()

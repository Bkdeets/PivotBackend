from django.db import models

# Don't store redundant data that Alpaca already stores

# Django User model

class Profile(models.Model):
    bio = models.CharField(max_length=200, null=True)


class Strategy(models.Model):
    name = models.CharField(max_length=200, null=True)
    isProfitable = models.BooleanField()

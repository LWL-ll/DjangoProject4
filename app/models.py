from django.db import models

# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32, null=True, blank=True)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=2)
    data = models.IntegerField(null=True, blank=True)
class Department(models.Model):
    title = models.CharField(max_length=16)
class Role(models.Model):
    caption = models.CharField(max_length=16)
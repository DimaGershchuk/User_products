from django.db import models
from django.contrib.auth.models import AbstractUser


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')], null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)



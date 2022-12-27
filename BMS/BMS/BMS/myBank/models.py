from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class form(models.Model):
    name=models.CharField(max_length=150)
    Fa_name=models.CharField(max_length=150)
    number=models.CharField(max_length=12)
    email=models.CharField(max_length=150)

    def __str__(self):
        return self.name
class Account(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    number=models.CharField(max_length=10)
    type=models.CharField(max_length=40)
    balance=models.CharField(max_length=40)
    def __str__(se):
        return se.user.username

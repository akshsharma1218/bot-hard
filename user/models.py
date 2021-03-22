from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone_reg = RegexValidator(regex=r'^\+?9?1?\d{9,10}$', message="Phone number must be entered in the format: '+91XXXXXXXXXX'.")
    phone_num = models.CharField(validators=[phone_reg], max_length=13, blank=True) # validators should be a list
    email     = models.EmailField()
    rel_num   = models.CharField(validators=[phone_reg], max_length=13, blank=True)
    anxiety   = models.IntegerField(null=True)


    def __str__(self):
        return self.username

from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from django_mysql.models import ListCharField


class User(AbstractUser):
    phone_reg = RegexValidator(regex=r'^\+?9?1?\d{9,10}$', message="Phone number must be entered in the format: '+91XXXXXXXXXX'.")
    phone_num = models.CharField(validators=[phone_reg], max_length=13, blank=True) # validators should be a list
    email     = models.EmailField()
    rel_num   = models.CharField(validators=[phone_reg], max_length=13, blank=True)
    anxiety   = models.IntegerField(null=True)
    diary     = models.TextField(null=True)
    list      = ListCharField(base_field = models.CharField(max_length=10), size = 30, max_length = 30 * 11)


    def __str__(self):
        return self.username

class Questions(models.Model):
    question_joy   = ListCharField(base_field = models.CharField(max_length=80), size = 20, max_length = 20 * 81)
    question_fear  = ListCharField(base_field = models.CharField(max_length=80), size = 20, max_length = 20 * 81)
    question_sad   = ListCharField(base_field = models.CharField(max_length=80), size = 20, max_length = 20 * 81)
    question_anger = ListCharField(base_field = models.CharField(max_length=80), size = 20, max_length = 20 * 81)

    def __str__(self):
        return 'Questions'

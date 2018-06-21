from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from .models import  models

class Notif(models.model):
    NotifId = models.IntegerField(max_length=8,blank=False,unique=True)
    Notifmessage=models.CharField(max_length=200,blank=False)
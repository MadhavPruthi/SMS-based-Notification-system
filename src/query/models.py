from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from .models import models

class queries(models.model):
    QueryId = models.IntegerField(max_length=8,blank=False,unique=True)
    CourseId = models.ForeignKey(Course, on_delete=models.CASCADE)
    QuryTo=models.CharField(max_length=50,blank=False)
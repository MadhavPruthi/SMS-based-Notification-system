from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

branches = [
        ("aero", "Aerospace"),
        ("civil", "Civil"),
        ("cse", "Computer Science"),
        ("ece", "Electronics & Communication"),
        ("elec", "Electrical"),
        ("mech", "Mechanical"),
        ("meta", "Materials & Metallurgical"),
        ("prod", "Production & Industrial"),
    ]
class Student(models.Model):
    years = [
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
    ]
    sem = [
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5", 5),
        ("6", 6),
        ("7", 7),
        ("8", 8),
        ]
    Student_ID = models.CharField(max_length=8, blank=False, unique=True)
    nmae = models.CharField(max_length=50)
    DOB = models.DateField(verbose_name="Date Of Birth")
    Branch = models.CharField(max_length=4, choices=branches, default="aero")
    Year_Of_Study = models.CharField(max_length=1, choices=years, default="1")
    Semester = models.CharField(max_length=1, choices=sem, default="1")
    Contact_Number = PhoneNumberField(blank=False)




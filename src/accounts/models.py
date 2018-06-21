from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Student(models.Model):

    User = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    StudentID = models.CharField(max_length=8, blank=False, unique=True)
    Name = models.CharField(max_length=50)
    Branch = models.CharField(max_length=50)
    YearOfStudy = models.IntegerField()
    ContactNumber = PhoneNumberField(blank=False)
    Email = models.EmailField(blank=False)


class Faculty(models.Model):

    User = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    FacultyID = models.CharField(max_length=8, blank=False, unique=True)
    Name = models.CharField(max_length=50)
    Department = models.CharField(max_length=50)
    Designation = models.CharField(max_length=30)
    ContactNumber = PhoneNumberField(blank=False)
    Email = models.EmailField(blank=False)


class Course(models.Model):

    CourseId = models.CharField(max_length=8, blank=False, unique=True)
    CourseName = models.CharField(max_length=250)


class StudentCourse(models.Model):

    CourseId = models.ForeignKey(Course, on_delete=models.CASCADE)
    StudentUser = models.ForeignKey(Student, on_delete=models.CASCADE)
    Semester = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)])


class FacultyCourse(models.Model):

    CourseId = models.ForeignKey(Course, on_delete=models.CASCADE)
    FacultyUser = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    Semester = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)])



from django.shortcuts import render, get_object_or_404
from .models import Student,Faculty
from django.contrib import messages

def Student(request):
    if request.method == 'POST':
            post=Student()
            post.user= request.user
            post.StudentID= request.user
            post.Name= request.user
            post.Branch=request.user
            post.YearOfStudy=request.user
            post.ContactNumber=request.user
            post.Email=request.user
            post.save()
    messages.success(request, "Your account has been created")
        return render(request, 'templates/signupForm.html')



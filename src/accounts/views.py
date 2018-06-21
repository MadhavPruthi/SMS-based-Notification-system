from .models import Student,Faculty
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404


def SignUpView(request):
    if request.method == 'POST':
        if request.POST['action'] == "student":

            form = AuthenticationForm(data=request.POST)

            if form.is_valid():
                post=Student()
                request.session['user'] = 'student'
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
        else:
            form = AuthenticationForm(data=request.POST)

            if form.is_valid():
                p=Faculty()
                request.session['user'] = 'staff'
                p.user = request.user
                p.FacultyID=request.user
                p.Name=request.user
                p.Department=request.user
                p.Designation=request.user
                p.ContactNumber=request.user
                p.Email=request.user
                p.save()
                messages.success(request, "Your account has been created")
                return render(request, 'templates/signupForm.html')
    else:
        pass


def LoginView(request):

    if request.method == "POST":

        if request.POST['action'] == "student":

            form = AuthenticationForm(data=request.POST)

            if form.is_valid():

                user = form.get_user()
                request.session['user'] = 'student'
                login(request, user)
                return HttpResponse('You are logged in Student')

        else:

            form = AuthenticationForm(data=request.POST)

            if form.is_valid():

                user = form.get_user()
                request.session['user'] = 'staff'
                login(request, user)
                return HttpResponse('You are logged in Staff')

    else:
        pass




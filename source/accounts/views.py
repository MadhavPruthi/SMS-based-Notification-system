from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from source.accounts.forms import SignUpStudentForm, SignUpFacultyForm
from source.accounts.models import Student, Faculty


def LoginView(request):



    if request.method == "POST":

        if request.POST['action'] == "student":

            form = AuthenticationForm(data=request.POST)

            if form.is_valid():

                user = form.get_user()
                request.session['user'] = 'student'
                request.session['username'] = Student.StudentID
                login(request, user)
                return HttpResponse('You are logged in Student')

        else:

            form = AuthenticationForm(data=request.POST)

            if form.is_valid():

                user = form.get_user()
                request.session['user'] = 'staff'
                request.session['username'] = Faculty.FacultyID
                login(request, user)
                return HttpResponse('You are logged in Staff')

    else:

        return render(request, 'accounts/loginForm.html' ,{})


def SignUpView(request):

    if request.method == "POST":

        if request.POST['action'] == "student":

            form = SignUpStudentForm(request.POST)

            if form.is_valid():

                instance = form.save(commit=False)

                username = form.cleaned_data.get('StudentID')
                password = form.cleaned_data.get('password')

                user = User.objects.create_user(username=username)
                user.set_password(password)
                user.save()

                instance.user = user
                instance.save()

                user = authenticate(username=username, password=password)
                login(request, user)
                print("Done")

                return redirect('main')

            else:
                return render(request, 'accounts/signupForm.html', {})

        else:

            form = SignUpFacultyForm(request.POST)

            if form.is_valid():
                pass

    else:

        return render(request, 'accounts/signupForm.html', {})

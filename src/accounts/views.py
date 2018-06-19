from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,redirect


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



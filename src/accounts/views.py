
from django.contrib.auth import login, authenticate
from .forms import Student_signup_form
from django.shortcuts import render,redirect

def signup(request):
    if request.method == 'POST':
        form = Student_signup_form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = Student_signup_form()
    return render(request, 'Student_Sign_Up.html', {'form': form})





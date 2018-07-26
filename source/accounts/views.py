from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.middleware import get_user
from django.contrib.auth.models import User
from django.contrib.auth.views import logout
from django.shortcuts import render, redirect
from source.Notification.models import Message
from source.accounts.forms import SignUpStudentForm, SignUpFacultyForm, FacultyCoursesForm, StudentCoursesForm
from source.accounts.models import Student, Faculty
from django.http import JsonResponse
from source.query.models import Question, Answer


def LoginView(request):


    if request.method == "POST" and request.is_ajax():

        form = AuthenticationForm(data=request.POST)

        if form.is_valid():

            if request.POST['action'] == "student":

                user = form.get_user()

                if Student.objects.filter(User__exact=user).exists():

                    login(request, user)
                    request.session['user'] = 'student'
                    request.session['username'] = user.username

                    return JsonResponse({"response": 'You are logged in Student', "working":"yes"})

                response = "It seems you are authenticated as Staff Member.Kindly login from Staff Section"

            else:

                user = form.get_user()

                if Faculty.objects.filter(User__exact=user).exists():

                    login(request, user)
                    request.session['user'] = 'staff'
                    request.session['username'] = user.username
                    return JsonResponse({"response": 'You are logged in Staff'})

                response = "It seems you are authenticated as Student Member.Kindly login from Student Section"

        if form.errors:
            return JsonResponse({"response": '''Please enter a correct username and password''', "working":"no" })
        else:
            return JsonResponse({"response": response, "working":"no"})


    try:
        ID = request.session['username']
    except:
        ID = None

    if ID:
         return redirect('accounts:profile')

    return render(request, 'accounts/loginForm.html', {})


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

                instance.User = user
                instance.save()

                # Adding Student to respective group
                instance.add_into_group()

                if user.is_authenticated():
                    request.session['user'] = 'student'
                    request.session['username'] = instance.StudentID
                    login(request, user)

                return redirect('main')

            else:

                context = {}
                if form.errors:
                    context = {
                        "errors":form.errors
                    }

                return render(request, 'accounts/signupForm.html', context)

        else:

            form = SignUpFacultyForm(request.POST)

            if form.is_valid():

                instance = form.save(commit=False)

                username = form.cleaned_data.get('FacultyID')
                password = form.cleaned_data.get('password')

                user = User.objects.create_user(username=username)
                user.set_password(password)
                user.save()

                instance.User = user
                instance.save()

                # Adding Faculty to Fac group
                instance.add_into_group()

                if user.is_authenticated():
                    request.session['user'] = 'staff'
                    request.session['username'] = instance.FacultyID
                    login(request, user)

                return redirect('main')

            else:

                context = {}
                if form.errors:
                    context = {
                        "errors": form.errors
                    }

                return render(request, 'accounts/signupForm.html', context)

    else:

        return render(request, 'accounts/signupForm.html', {})


@login_required()
def ProfileView(request):

    ID = request.session['username']
    user_type = request.session['user']

    if user_type == 'student':

        object = Student.objects.get(StudentID__exact=ID)
        all_groups = request.user.groups.all()
        all_messages = Message.objects.filter(SentFor__in=all_groups).order_by('-DateTime')[:6]
        form = StudentCoursesForm()
        all_teachers = Faculty.objects.filter(Courses__faculty__Courses__in=object.Courses.all()).distinct()
        Responses = Answer.objects.filter(Question__QueriedBy=ID).filter(Question__IsAnswered=True).order_by('-AnsweredAt')

        context = {
            "object": object,
            "all_messages": all_messages,
            "form": form,
            "all_teachers":all_teachers,
            "Responses": Responses,
        }

        return render(request, 'accounts/Student_Home.html', context)

    elif user_type == 'staff':
        object = Faculty.objects.get(FacultyID__exact=ID)
        all_messages = Message.objects.filter(SentBy__exact=request.user).order_by('-DateTime')[:6]
        form = FacultyCoursesForm()
        Questions = Question.objects.filter(CreatedFor__exact=get_user(request)).filter(IsAnswered=False)

        context = {
            "object":object,
            "all_messages":all_messages,
            "form":form,
            "Questions":Questions,
        }

        return render(request, 'accounts/Faculty_Home.html', context)


@login_required()
def LogoutView(request):

    logout(request)
    return redirect('accounts:login')

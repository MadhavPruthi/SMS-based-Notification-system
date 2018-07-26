from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from source.query.models import Question, Answer


@login_required()
def QuestionHandlingView(request):

    if request.method == "POST" and request.is_ajax():

        values = request.POST

        Queobj = Question()
        Queobj.QuestionTitle = values['QuestionTitle']
        if values['CreatedFor'] and values['QuestionTitle']:
            Queobj.CreatedFor = User.objects.get(username__exact=values['CreatedFor'])
            Queobj.QueriedBy = str(request.user)
            Queobj.save()

            return JsonResponse({"working":"yes"})

        else:

            return JsonResponse({"response": "Kindly fill all the values before submitting query!", "working": "no"})


@login_required()
def AnswerHandlingView(request):

    if request.method == "POST":
        values = request.POST

        AnsObj = Answer()
        AnsObj.AnswerTitle = values['AnswerTitle']
        Queobj = Question.objects.get(pk=values['pk'])
        AnsObj.Question = Queobj
        Queobj.IsAnswered = True
        Queobj.save()
        AnsObj.save()

        return redirect(request.META['HTTP_REFERER'])



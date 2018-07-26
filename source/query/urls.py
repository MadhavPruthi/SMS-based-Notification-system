from django.conf.urls import url
from source.query.views import QuestionHandlingView, AnswerHandlingView

app_name = "query"

urlpatterns = [
    url(r'ask/$' , QuestionHandlingView, name="QuestionAsk"),
    url(r'answer/$' , AnswerHandlingView, name="QuestionAnswer")
]
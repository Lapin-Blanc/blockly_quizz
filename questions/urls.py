# questions.urls
from django.urls import path
from questions.views import index, detail, answer, exam, exams_list

app_name = 'questions'
urlpatterns = [
    path('', index, name='index'),
    path('<int:question_id>/', detail, name='detail'),
    path('answer/<int:answer_id>/', answer, name='answer'),
    path('exam/<int:exam_id>/', exam, name='exam'),
    path('exams_list/', exams_list, name='exams_list'),
]

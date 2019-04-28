from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from questions.models import Question, Answer, Exam
from questions.forms import AnswerForm

# Create your views here.

def detail(request, question_id):
  question = get_object_or_404(Question, pk=question_id)
  return render(request, 'question_detail.html', {'question':question})


def answer(request, answer_id):
  answer = get_object_or_404(Answer, pk=answer_id)
  # ~ if request.method == 'POST':
    # ~ form = AnswerForm(request.POST, instance=answer)
    # ~ if form.is_valid() :
      # ~ form.save()
      # ~ return HttpResponseRedirect(reverse("questions:answer", args=[answer_id]))
      
  # ~ form = AnswerForm(instance=answer)
  return render(request, 'answer_detail.html', {'answer':answer})


def exam(request, exam_id):
  exam = get_object_or_404(Exam, pk=exam_id)
  answer = exam.answer_set.filter(answered=False).first()
  if not answer:
    exam.complete = True
    exam.save()
    return HttpResponseRedirect(reverse("questions:exams_list"))
  if request.method == 'POST':
    form = AnswerForm(request.POST, instance=answer)
    form.data = form.data.copy()
    form.data['answered'] = True
    if form.is_valid() :
      form.save()
      return HttpResponseRedirect(reverse("questions:exam", args=[exam_id]))
  
  
  form = AnswerForm(instance=answer)
  return render(request, 'exam_detail.html', {'form':form, 'question':answer.question})


def exams_list(request):
  exams = Exam.objects.filter(student=request.user, complete=False)
  return render(request, 'exams_list.html', {'exams':exams})

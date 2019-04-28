from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
  short_name = models.CharField(max_length=50)
  states = RichTextField()
  toolbox = models.TextField(null=True, blank=True)
  workspace = models.TextField(null=True, blank=True)
  
  def get_absolute_url(self):
    return reverse('questions:detail', args=[str(self.id)])
  
  def __str__(self):
    return self.short_name


class Questionnaire(models.Model):
  short_name = models.CharField(max_length=50)
  questions = models.ManyToManyField(Question)
  
  def __str__(self):
    return self.short_name
    
    
class Answer(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  exam = models.ForeignKey('Exam', on_delete=models.CASCADE, null=True)
  answer = models.TextField(null=True, blank=True)
  remark = models.TextField(null=True, blank=True)
  answered = models.BooleanField(default=False)
  date_modified = models.DateTimeField(auto_now_add=True)
  
  def get_absolute_url(self):
    return reverse('questions:answer', args=[str(self.id)])

  def __str__(self):
    return self.question.short_name


class Exam(models.Model):
  short_name = models.CharField(max_length=50, null=True)
  student = models.ForeignKey(User, on_delete=models.CASCADE)
  date_created = models.DateTimeField(auto_now=True)
  # ~ date_modified = models.DateTimeField(auto_now_add=True)
  # ~ questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
  
  def get_absolute_url(self):
    return reverse('questions:exam', args=[str(self.id)])

  def save(self, *args, **kwargs):
    super(Exam, self).save(*args, **kwargs)
    if self.answer_set.count() == 0:
      for q in self.questionnaire.questions.all():
        self.answer_set.create(question=q)

  def __str__(self):
    return "{} - {}".format(self.student, self.short_name)

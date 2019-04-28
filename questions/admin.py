from django.contrib import admin

# Register your models here.
from questions.models import Question, Questionnaire, Exam, Answer

class AnswerInline(admin.TabularInline):
  model = Answer
  extra = 0

class ExamAdmin(admin.ModelAdmin):
  list_display = ('short_name', 'student')
  list_filter = ('short_name', 'student')
  inlines = (AnswerInline,)

class AnswerAdmin(admin.ModelAdmin):
  list_display = ('question', 'exam', 'get_date_created')
  list_filter = ('exam',)
  def get_date_created(self, obj):
      return obj.exam.date_created
  get_date_created.admin_order_field  = 'date_created'  #Allows column order sorting
  get_date_created.short_description = 'Date de création'  #Renames column head

class QuestionnaireAdmin(admin.ModelAdmin):
  filter_horizontal = ('questions',)

admin.site.register(Question)
admin.site.register(Questionnaire, QuestionnaireAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Exam, ExamAdmin)

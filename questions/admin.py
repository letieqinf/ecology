from django.contrib import admin
from .models import ImageAnswer, Question, ImageQuestion, Answer

# Register your models here.

class AnswerInline(admin.TabularInline):
    model = Answer

class ImageAnswerInline(admin.TabularInline):
    model = ImageAnswer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

class ImageQuestionAdmin(admin.ModelAdmin):
    inlines = [ImageAnswerInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(ImageQuestion, ImageQuestionAdmin)
admin.site.register(Answer)
admin.site.register(ImageAnswer)
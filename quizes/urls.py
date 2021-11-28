from django.contrib import admin
from django.urls import path, re_path

from .views import (
    QuizList,
    quiz_view,
    quiz_data_view,
    save_quiz_view
)

urlpatterns = [
    path('', QuizList.as_view(), name='quizes'),
    path('<pk>/', quiz_view, name='quiz'),
    path('<pk>/save/', save_quiz_view, name='quiz_save'),
    path('<pk>/data/', quiz_data_view, name='quiz_data')
]
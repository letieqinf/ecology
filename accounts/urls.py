from django import template
from django.contrib import admin
from django.urls import path, re_path

from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView

from .views import *


urlpatterns = [
    # path('', Home.as_view(), name='account'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', LogOut.as_view(), name='logout'),
    path('profile/', Profile.as_view(), name='profile')
]
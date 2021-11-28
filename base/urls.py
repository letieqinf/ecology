from django.contrib import admin
from django.urls import path, re_path

from .views import *


urlpatterns = [
    path('', Home.as_view(), name='index'),
    path('map/', Map.as_view(), name='map')
]
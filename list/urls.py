from django.contrib import admin
from django.urls import path, re_path

from .views import *


urlpatterns = [
    path('', List.as_view(), name='list'),
    path('mac/', Mac.as_view(), name='mac'),
    path('metal/', Metal.as_view(), name='metal'),
    path('glass/', Glass.as_view(), name='glass'),
    path('plastic/', Plastic.as_view(), name='plastic'),
    path('box/', Box.as_view(), name='box'),
    path('wastes/', Wastes.as_view(), name='wastes'),
    path('clothes/', Clothes.as_view(), name='clothes')
]
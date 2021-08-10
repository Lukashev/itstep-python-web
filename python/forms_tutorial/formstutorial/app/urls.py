from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('task2', task2),
    path('task3', task3),
    path('task4', task4)
]
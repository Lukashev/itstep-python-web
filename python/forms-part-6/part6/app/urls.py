from django.urls import path
from .views import *

urlpatterns = [
    path('', task1),
    path('task3', task3)
]
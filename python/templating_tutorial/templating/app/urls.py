from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index),
    path('football/', football),
    path('basketball/', basketball),
    path('hockey/', hockey)
]

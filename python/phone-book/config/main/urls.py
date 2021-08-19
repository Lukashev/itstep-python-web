from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="phone_book-list"),
    path('add_phone_record', add_phone_record, name="add_phone_record")
]

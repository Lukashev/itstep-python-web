from django.urls import path
from .views import *

app_name = 'app'

urlpatterns = [
    path('', index, name='article-list-all'),
    path('article/<str:slug>/', index, name='article-list'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout),
    path('register/', user_register, name='register'),
    path('add_article', add_article, name='add_article'),
    path('article_details/<int:article_id>/<str:slug>/', article_details, name='article_details')
]

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .models import Category, Article
from .forms import *

#  Category.objects.annotate(num_products=Count('products'))

def index(request, slug=None):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    if not slug:
        articles = Article.objects.all()
    else:
        category = get_object_or_404(Category, slug=slug)
        articles = Article.objects.filter(category=category)
    context = {**context, 'articles': articles}
    return render(request, 'index.html', context)


def add_article(request):
    return render(request, 'add_article.html')


def article_details(request, article_id=None, slug=None):
    article = get_object_or_404(Article, pk=article_id, slug=slug)
    categories = Category.objects.all()
    context = {
        'article': article,
        'categories': categories
    }
    return render(request, 'article_details.html', context)


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            messages.success(request, 'Вы успешно выполнили вход в систему')
            user = form.get_user()
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Вы ввели некорректные данные')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('/login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html',{'form': form})


def user_logout(request):
    logout(request)
    return redirect('/login')
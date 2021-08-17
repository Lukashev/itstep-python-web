from django.shortcuts import render
from .forms import *
from django.conf import settings
import math
import json

with open(str(settings.BASE_DIR) + '\static\\books.json', encoding='utf-8') as file:
    data = json.loads(file.read())

def handle_post(form, request):
    body = {**request.POST}
    print(body)
    del body['csrfmiddlewaretoken']
    result = []
    for field in body:
        result.append({'label': form[field].label, 'value': body[field][0]})
    return result


def task1(request):
    form = WaterDeliveryForm()
    response = None
    if request.method == 'POST':
        response = handle_post(form, request)
    return render(request, 'task1.html', {'form': form, 'title': 'Water Delivery', 'response': response})


def task3(request):
    current_page = int(request.GET.get('page', 1))
    search_query = request.GET.get('search_query', None) or request.POST.get('search_query', '')
    # print(search_query, current_page, sep=':')
    form = SearchForm(request.POST)

    current_books = data.get('books')
    filtered_books = list(filter(lambda b: search_query.lower() in b['title'].lower() if search_query else True, current_books))

    pagination_count = math.ceil(len(filtered_books) / 10)
    pag_start = (current_page-1)*10
    pag_end = (current_page-1)*10+10
    books_per_page = filtered_books[pag_start:pag_end]

    return render(request, 'task3.html', {
        'title': 'Сайт книг',
        'form': form,
        'current_books': books_per_page,
        'search_result_count': len(filtered_books),
        'pagination_count': range(1, pagination_count + 1),
        'search_query': search_query
    })
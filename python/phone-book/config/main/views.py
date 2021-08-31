from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib import messages
from .models import PhoneBook
from .forms import AddContactForm


def index(request):
    search_query = request.POST.get('search_query')
    if request.method == 'POST' and not search_query:
        current_id = request.POST.get('id', None)
        contact = get_object_or_404(pk=current_id, klass=PhoneBook)
        contact.delete()
        phone_book_list = PhoneBook.objects.all()
    elif request.method == 'POST' and search_query:
        print(search_query)
        phone_book_list = PhoneBook.objects.filter(
            Q(first_name__icontains=search_query)
            | Q(last_name__icontains=search_query)
            | Q(phone_number__contains=search_query)
        )
    else:
        phone_book_list = PhoneBook.objects.all()

    print(phone_book_list)
    return render(request, 'index.html', {'phone_book_list': phone_book_list})


def add_phone_record(request):
    if request.method == 'GET':
        form = AddContactForm()
    else:
        form = AddContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно добавили контакт')
            return redirect('/')
    return render(request, 'add_contact.html', {'form': form})


def update_item(request, contact_id):
    if request.method == 'GET':
        contact = get_object_or_404(pk=int(contact_id), klass=PhoneBook)
        form = AddContactForm(instance=contact)
    else:
        form = AddContactForm(request.POST)
        body = {**request.POST}
        del body['csrfmiddlewaretoken']
        del body['id']
        for key in body:
            body[key] = body[key][0]
        print(body)
        obj, created = PhoneBook.objects.update_or_create(pk=int(request.POST.get('id')), defaults={**body})
        print(obj, created)
        # contact = get_object_or_404(pk=int(request.POST.get('id')), klass=PhoneBook)
        # contact.first_name = request.POST.get('first_name')
        # contact.last_name = request.POST.get('last_name')
        # contact.phone_number = request.POST.get('phone_number')
        # contact.email = request.POST.get('email')
        # contact.note = request.POST.get('note')
        # contact.save()
        return redirect('/')
    return render(request, 'update_item.html', {'form': form, 'contact_id': contact_id})

from django.shortcuts import render, redirect, get_object_or_404
from .models import PhoneBook
from .forms import AddContactForm

def index(request):
    if request.method == 'POST':
        current_id = request.POST.get('id', None)
        contact = get_object_or_404(pk=current_id, klass=PhoneBook)
        contact.delete()
    phone_book_list = PhoneBook.objects.all()
    return render(request, 'index.html', {'phone_book_list': phone_book_list})


def add_phone_record(request):
    if request.method == 'GET':
        form = AddContactForm()
    else:
        form = AddContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'add_contact.html', {'form': form})

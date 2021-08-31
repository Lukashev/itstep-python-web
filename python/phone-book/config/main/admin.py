from django.contrib import admin
from .models import PhoneBook

class PhoneBookAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number')


admin.site.register(PhoneBook, PhoneBookAdmin)

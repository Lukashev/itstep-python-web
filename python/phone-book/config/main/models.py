from django.db import models

class PhoneBook(models.Model):
    first_name = models.CharField(max_length=64, blank=False)
    last_name = models.CharField(max_length=64, blank=False)
    email = models.EmailField(max_length=64, blank=True)
    phone_number = models.CharField(max_length=64, blank=False, unique=True)
    note = models.TextField(default='N/A')

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone_number}"

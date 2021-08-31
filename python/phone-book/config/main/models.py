from django.db import models

class PhoneBook(models.Model):
    first_name = models.CharField(max_length=64, blank=False, verbose_name='Имя')
    last_name = models.CharField(max_length=64, blank=False, verbose_name='Фамилия')
    email = models.EmailField(max_length=64, blank=True, verbose_name='Почта')
    phone_number = models.CharField(max_length=64, blank=False, unique=True, verbose_name='Телефон')
    note = models.TextField(default='N/A', verbose_name='Заметка')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.phone_number}"

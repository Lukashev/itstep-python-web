from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=64, blank=False, verbose_name='Имя')
    last_name = models.CharField(max_length=64, blank=False, verbose_name='Фамилия')
    email = models.EmailField(max_length=64, blank=True, null=True, verbose_name='Почта')
    phone = models.CharField(max_length=32, blank=False, verbose_name='Номер телефона')

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'

    def __str__(self):
        return self.first_name + " " + self.last_name


class Seller(models.Model):

    POSITION_CHOICES = [
        (0, 'Продавец'),
        (1, 'Старший продавец'),
        (2, 'Руководитель отдела продаж')
    ]

    first_name = models.CharField(max_length=64, blank=False, verbose_name='Имя')
    last_name = models.CharField(max_length=64, blank=False, verbose_name='Фамилия')
    email = models.EmailField(max_length=64, blank=True, null=True, verbose_name='Почта')
    phone = models.CharField(max_length=32, blank=False, verbose_name='Номер телефона')
    date = models.DateField(blank=False, verbose_name='Дата контракта')
    position = models.IntegerField(
        blank=False,
        choices=POSITION_CHOICES,
        default=0,
        verbose_name='Должность'
    )

    class Meta:
        verbose_name = 'Продавец'
        verbose_name_plural = 'Продавцы'


class Product(models.Model):
    name = models.CharField(max_length=64, blank=False, verbose_name='Наименование')
    description = models.TextField(blank=True, default='', verbose_name='Описание')
    image = models.ImageField(upload_to='product_images/%Y/%m/%d', verbose_name='Изображение')
    stock = models.IntegerField(blank=True, default=0, verbose_name='В наличии (шт)')
    price = models.DecimalField(max_digits=19, decimal_places=2, default=0, verbose_name='Цена')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Order(models.Model):
    customer = models.ForeignKey(
        'Customer',
        on_delete=models.CASCADE,
        related_name='orders',
        related_query_name='order',
        verbose_name='Покупатель'
    )
    seller = models.ForeignKey(
        'Seller',
        on_delete=models.CASCADE,
        related_name='sellers',
        related_query_name='seller',
        verbose_name='Продавец'
    )
    product = models.ForeignKey(
        'Product',
        on_delete=models.CASCADE,
        related_name='products',
        related_query_name='product',
        verbose_name='Продукт'
    )
    date = models.DateField(auto_now_add=True, verbose_name='Дата заказа')
    total = models.DecimalField(max_digits=19, decimal_places=2, default=0, verbose_name='Сумма продажи')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
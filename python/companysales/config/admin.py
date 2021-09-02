from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'email', 'phone']


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'email', 'phone', 'date', 'position']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'stock', 'price', 'product_image']
    readonly_fields = ['product_image']


    def product_image(self, obj):
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url=obj.image.url,
            width=obj.image.width / 2,
            height=obj.image.height / 2,
            )
        )

    product_image.short_description = 'Изображение'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

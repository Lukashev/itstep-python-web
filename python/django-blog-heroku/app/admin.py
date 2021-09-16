from django.contrib import admin
from .models import *
from django import forms
from ckeditor.widgets import CKEditorWidget


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Article
        fields = '__all__'


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    list_display = ['title', 'category', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Article, ArticleAdmin)
from django.db import models
from django.urls import reverse
from os import path


def get_upload_path(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return path.join('images/', filename)


class Category(models.Model):
    name = models.CharField(max_length=150, blank=False, db_index=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=150, unique=True, blank=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app:article-list', kwargs={'slug': self.slug})


class Article(models.Model):
    title = models.CharField(max_length=256, blank=False, verbose_name='Название')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', verbose_name='Категория')
    slug = models.SlugField(max_length=256, db_index=True)
    content = models.TextField(blank=True, default='Нет описания')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    image = models.ImageField(upload_to=get_upload_path, blank=True)

    class Meta:
        ordering = ('title',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('app:article_details', args=[self.id, self.slug])
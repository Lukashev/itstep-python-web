# Generated by Django 3.2.6 on 2021-08-07 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('title',), 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='name',
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=256),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата обновления'),
        ),
    ]

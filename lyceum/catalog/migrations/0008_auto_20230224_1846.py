# Generated by Django 3.2.16 on 2023-02-24 13:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20230224_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Укажите имя', max_length=150, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(help_text='Назовите категорию', unique=True, validators=[django.core.validators.MaxLengthValidator(200)], verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(help_text='Укажите имя', max_length=150, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(help_text='Укажите имя', max_length=150, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(help_text='Назовите тег', unique=True, validators=[django.core.validators.MaxLengthValidator(200)], verbose_name='Название тега'),
        ),
    ]

# Generated by Django 3.2.16 on 2023-02-24 21:07

import django.core.validators
from django.db import migrations, models

import core.models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0012_auto_20230225_0207"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="text",
            field=models.TextField(
                default="Превосходно и роскошно",
                help_text="Опишите товар",
                validators=[core.models.custom_validator],
                verbose_name="Описание товара",
            ),
        ),
        migrations.AlterField(
            model_name="tag",
            name="canonical_name",
            field=models.CharField(
                default=models.SlugField(
                    help_text="Назовите тег",
                    unique=True,
                    validators=[
                        django.core.validators.MaxLengthValidator(200)
                    ],
                    verbose_name="Название тега",
                ),
                help_text="АБОБА",
                max_length=150,
                unique=True,
                verbose_name="секретное имя",
            ),
        ),
    ]
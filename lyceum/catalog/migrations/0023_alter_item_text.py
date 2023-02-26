# Generated by Django 3.2.16 on 2023-02-26 10:58

from django.db import migrations, models

import core.models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0022_alter_item_text"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="text",
            field=models.TextField(
                default="Превосходно и роскошно",
                help_text="Опишите товар",
                validators=[core.models.custom_validator],
                verbose_name="описание товара",
            ),
        ),
    ]

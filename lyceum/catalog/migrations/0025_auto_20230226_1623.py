# Generated by Django 3.2.16 on 2023-02-26 11:23

from django.db import migrations, models

import core.models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0024_alter_item_text"),
    ]

    operations = [
        migrations.AddField(
            model_name="tag",
            name="canonical_name",
            field=models.CharField(default="DEFAULT", max_length=150),
        ),
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

# Generated by Django 3.2.16 on 2023-02-24 14:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0008_auto_20230224_1846"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="catalog_items",
                to="catalog.category",
                verbose_name="каталог",
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="tags",
            field=models.ManyToManyField(
                to="catalog.Tag", verbose_name="теги"
            ),
        ),
    ]

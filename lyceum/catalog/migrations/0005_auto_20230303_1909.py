# Generated by Django 3.2.16 on 2023-03-03 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_mainimagemodel_item'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallerymodel',
            options={'verbose_name': 'галерея', 'verbose_name_plural': 'галерея'},
        ),
        migrations.AlterModelOptions(
            name='mainimagemodel',
            options={'verbose_name': 'превью', 'verbose_name_plural': 'превью'},
        ),
    ]

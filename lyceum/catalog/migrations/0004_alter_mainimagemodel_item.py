# Generated by Django 3.2.16 on 2023-03-03 14:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20230303_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainimagemodel',
            name='item',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='catalog.item', verbose_name='товар'),
        ),
    ]

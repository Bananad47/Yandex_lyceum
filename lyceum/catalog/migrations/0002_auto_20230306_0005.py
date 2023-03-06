# Generated by Django 3.2.16 on 2023-03-05 19:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="is_on_main",
            field=models.BooleanField(
                default=False, verbose_name="на главной"
            ),
        ),
        migrations.AlterField(
            model_name="item",
            name="preview",
            field=models.ImageField(
                help_text="будет приведено к размеру 300x300",
                upload_to="catalog/preview",
                verbose_name="превью",
            ),
        ),
    ]

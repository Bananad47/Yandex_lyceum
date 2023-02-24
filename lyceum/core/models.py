from django.core.exceptions import ValidationError
from django.db import models


def custom_validator(value):
    value = value.lower().split()
    if "превосходно" not in value and "роскошно" not in value:
        raise ValidationError("Ваш текст не превосходен!")


class AbstractionModel(models.Model):
    is_published = models.BooleanField(
        "Опубликовано",
        default=True,
    )

    name = models.CharField(
        "Наименование",
        help_text="Укажите имя",
        max_length=150,
    )

    class Meta:
        abstract = True

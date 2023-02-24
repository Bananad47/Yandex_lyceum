import re

from django.core.exceptions import ValidationError
from django.db import models


def custom_validator(value):
    if re.findall(r"\b(превосходно|раскошно)\b", value.lower()) == []:
        raise ValidationError("Ваш текст не превосходен и не роскошен!")


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

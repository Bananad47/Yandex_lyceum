import re

from django.core.exceptions import ValidationError
from django.db import models


def custom_validator(*words):
    def validate(value):
        for word in words:
            if re.findall(r"\b({})\b".format(word), value.lower()) == []:
                raise ValidationError(f"Ваш текст не содержит слова {word}!")

    return validate


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

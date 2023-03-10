import re

from django.core.exceptions import ValidationError
from django.db import models

from transliterate import translit


class AbstractionModel(models.Model):
    is_published = models.BooleanField(
        "опубликовано",
        default=True,
    )

    name = models.CharField(
        "наименование",
        help_text="Укажите имя",
        max_length=150,
    )

    canonical_name = models.CharField(
        max_length=150,
        default="DEFAULT",
    )

    class Meta:
        abstract = True

    def generate_canonical_name(self) -> str:
        canonical_name = (
            "".join(
                re.findall(
                    r"[a-z0-9]",
                    translit(
                        self.name.lower(),
                        language_code="ru",
                        reversed=True,
                    ),
                )
            ),
        )

        print(canonical_name, self.name.lower())
        return canonical_name

    def clean(self):
        self.canonical_name = self.generate_canonical_name()
        cnt = (
            type(self)
            .objects.filter(canonical_name=self.canonical_name)
            .exclude(id=self.id)
            .count()
        )

        if cnt != 0:
            raise ValidationError("Элемент с таким именем уже существует!")
        return super().clean()

    def __str__(self):
        return self.name

import re

from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator
from django.db import models

from core.models import AbstractionModel, custom_validator
from transliterate import translit


class Tag(AbstractionModel):
    slug = models.SlugField(
        "название тега",
        unique=True,
        help_text="Назовите тег",
        validators=[
            MaxLengthValidator(200),
        ],
    )

    canonical_name = models.CharField(
        max_length=150,
        default="DEFAULT",
    )

    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"

    def generate_canonical_name(self) -> str:
        canonical_name = translit(
            "".join(re.findall(r"\w", self.name.lower())),
            language_code="ru",
            reversed=True,
        )

        return canonical_name

    def save(self, *args, **kwargs):  # noqa: FNE003
        self.canonical_name = self.generate_canonical_name()
        super().save(*args, **kwargs)

    def clean(self):
        self.canonical_name = self.generate_canonical_name()
        cnt = (
            Tag.objects.filter(canonical_name=self.canonical_name)
            .exclude(id=self.id)
            .count()
        )

        if cnt != 0:
            raise ValidationError("Элемент с таким именем уже существует!")
        return super().clean()

    def __str__(self):
        return self.name


class Category(AbstractionModel):
    slug = models.SlugField(
        "название категории",
        unique=True,
        help_text="Назовите категорию",
        validators=[
            MaxLengthValidator(200),
        ],
    )

    weight = models.PositiveSmallIntegerField(
        "вес категории",
        help_text="Укажите вес категории",
        default=100,
    )

    canonical_name = models.CharField(
        max_length=150,
        default="DEFAULT",
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def generate_canonical_name(self) -> str:
        canonical_name = translit(
            "".join(re.findall(r"\w", self.name.lower())),
            language_code="ru",
            reversed=True,
        )

        return canonical_name

    def save(self, *args, **kwargs):  # noqa: FNE003
        self.canonical_name = self.generate_canonical_name()
        super().save(*args, **kwargs)

    def clean(self):
        self.canonical_name = self.generate_canonical_name()
        cnt = (
            Category.objects.filter(canonical_name=self.canonical_name)
            .exclude(id=self.id)
            .count()
        )

        if cnt != 0:
            raise ValidationError("Элемент с таким именем уже существует!")
        return super().clean()

    def __str__(self):
        return self.name


class Item(AbstractionModel):
    text = models.TextField(
        "описание товара",
        help_text="Опишите товар",
        validators=[
            custom_validator("превосходно", "роскошно"),
        ],
        default="Превосходно и роскошно",
    )

    category = models.ForeignKey(
        "category",
        on_delete=models.CASCADE,
        related_name="catalog_items",
        verbose_name="каталог",
    )

    tags = models.ManyToManyField(
        Tag,
        verbose_name="теги",
    )

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"

    def __str__(self):
        return self.name

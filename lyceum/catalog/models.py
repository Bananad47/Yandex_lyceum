from django.core.validators import MaxLengthValidator
from django.db import models

from core.models import AbstractionModel, custom_validator


class Tag(AbstractionModel):
    slug = models.SlugField(
        "Название тега",
        unique=True,
        help_text="Назовите тег",
        validators=[
            MaxLengthValidator(200),
        ],
    )

    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"

    def __str__(self):
        return self.name


class Category(AbstractionModel):
    slug = models.SlugField(
        "Название категории",
        unique=True,
        help_text="Назовите категорию",
        validators=[
            MaxLengthValidator(200),
        ],
    )

    weight = models.PositiveSmallIntegerField(
        "Вес категории",
        help_text="Укажите вес категории",
        default=100,
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name


class Item(AbstractionModel):
    text = models.TextField(
        "Описание товара",
        help_text="Опишите товар",
        validators=[
            custom_validator,
        ],
        default="Превосходно",
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

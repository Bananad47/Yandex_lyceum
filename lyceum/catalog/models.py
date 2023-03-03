from django.core.validators import MaxLengthValidator
from django.db import models

from core.models import AbstractionImageModel, AbstractionModel
from core.validators import custom_validator


class Tag(AbstractionModel):
    slug = models.SlugField(
        "название тега",
        unique=True,
        help_text="Назовите тег",
        validators=[
            MaxLengthValidator(200),
        ],
    )

    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"


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

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"


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


class MainImageModel(AbstractionImageModel):
    item = models.OneToOneField(
        Item,
        on_delete=models.CASCADE,
        primary_key=True,
        verbose_name="товар",
    )

    class Meta:
        verbose_name = "превью"
        verbose_name_plural = "превью"


class GalleryModel(AbstractionImageModel):
    item = models.ForeignKey(
        "item",
        on_delete=models.CASCADE,
        related_name="gallery_items",
        verbose_name="товар",
    )

    class Meta:
        verbose_name = "галерея"
        verbose_name_plural = "галерея"

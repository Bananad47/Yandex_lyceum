from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator
from django.db import models


def custom_validator(value):
    value = value.lower()
    if "превосходно" not in value and "роскошно" not in value:
        raise ValidationError("Ваш текст не превосходен!")


class Tag(models.Model):
    is_published = models.BooleanField(
        "Опубликовано",
        help_text="Скройте или опубликуйте тег",
        default=True,
    )

    name = models.TextField(
        "Наименование тега",
        help_text="Назовите тег",
        validators=[
            MaxLengthValidator(150),
        ],
    )

    slug = models.SlugField(
        "Название тега",
        unique=True,
        help_text="Роскошный и превосходный текст про тег",
        validators=[
            MaxLengthValidator(200),
        ],
    )

    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"

    def __str__(self):
        return self.slug


class Category(models.Model):
    is_published = models.BooleanField(
        "Опубликовано",
        help_text="Скройте или опубликуйте категорию",
        default=True,
    )

    name = models.TextField(
        "Наименование категории",
        help_text="Назовите категорию",
        validators=[
            MaxLengthValidator(150),
        ],
    )

    slug = models.SlugField(
        "Название категории",
        unique=True,
        help_text="Роскошный и превосходный текст про категорию",
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
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.slug


class Item(models.Model):
    is_published = models.BooleanField(
        "Опубликовано",
        help_text="Скройте или опубликуйте товар",
        default=True,
    )

    name = models.TextField(
        "Наименование товара",
        help_text="Назовите товар",
        validators=[
            MaxLengthValidator(150),
        ],
        default="Гениальное наименование роскошного товара!",
    )

    text = models.TextField(
        "Описание товара",
        help_text="Опишите товар",
        validators=[
            custom_validator,
        ],
        default="Превосходное описание роскошного товара!",
    )

    category = models.ForeignKey(
        "category", on_delete=models.CASCADE, related_name="catalog_items"
    )

    tags = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name

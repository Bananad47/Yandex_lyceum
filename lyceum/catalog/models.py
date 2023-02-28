from django.core.validators import MaxLengthValidator
from django.db import models
from django.utils.safestring import mark_safe

from core.models import AbstractionModel
from core.validators import custom_validator
from sorl.thumbnail import get_thumbnail


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


class ImageModel(models.Model):
    image = models.ImageField(
        "будет приведено к ширине 1280px",
        upload_to="catalog",
    )

    def get_image_x1280(self):
        return get_thumbnail(self.image, "1280", quality=51)

    def get_image_400x300(self):
        return get_thumbnail(self.image, "400x300", quality=51, crop="center")

    def image_tmb(self):
        if self.image:
            return mark_safe(f"<img src='{self.image.url}' width='50'>")
        return "нет изображения"

    image_tmb.short_description = "превью"
    image_tmb.allow_tags = True

    class Meta:
        verbose_name = "изображение"
        verbose_name_plural = "изображения"

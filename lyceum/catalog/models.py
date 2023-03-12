from django.core.validators import MaxLengthValidator
from django.db import models
from django.db.models.functions import Lower
from django.utils.safestring import mark_safe

from core.models import AbstractionModel
from core.validators import custom_validator
from sorl.thumbnail import get_thumbnail


class Tag(AbstractionModel):
    slug = models.SlugField(
        "слаг тега",
        unique=True,
        help_text="слаг",
        validators=[
            MaxLengthValidator(200),
        ],
    )

    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"


class Category(AbstractionModel):
    slug = models.SlugField(
        "слаг категории",
        unique=True,
        help_text="слаг",
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


class GalleryManager(models.Manager):
    def item_gallery(self, item_id_):
        return self.get_queryset().filter(item_id=item_id_).only("image")


class ItemManager(models.Manager):
    def item_homepage(self):
        return (
            self.get_queryset()
            .select_related("category")
            .prefetch_related(
                models.Prefetch(
                    "tags",
                    queryset=Tag.objects.filter(
                        is_published=True,
                    ).only("name"),
                )
            )
            .filter(
                is_published=True, is_on_main=True, category__is_published=True
            )
            .only("name", "text", "preview", "category__name", "tags__name")
            .order_by("name")
        )

    def item_items_list(self):
        return (
            self.get_queryset()
            .select_related("category")
            .prefetch_related(
                models.Prefetch(
                    "tags",
                    queryset=Tag.objects.filter(
                        is_published=True,
                    ).only("name"),
                )
            )
            .filter(is_published=True, category__is_published=True)
            .only("name", "text", "preview", "category__name", "tags__name")
            .order_by(Lower("category__name"), Lower("name"))
        )


class GalleryModel(models.Model):
    objects = GalleryManager()
    image = models.ImageField(
        "будет приведено к размеру 300x300",
        upload_to="catalog/gallery",
    )

    item = models.ForeignKey(
        "item",
        on_delete=models.CASCADE,
        related_name="gallery_items",
        verbose_name="товар",
    )

    def get_image_300x300(self):
        return get_thumbnail(self.image, "300x300", quality=51, crop="center")

    def image_tmb(self):
        if self.image:
            return mark_safe(f"<img src='{self.image.url}' width='50'>")
        return "нет изображения"

    class Meta:
        verbose_name = "галерея"
        verbose_name_plural = "галерея"


class Item(AbstractionModel):
    objects = ItemManager()
    text = models.TextField(
        "описание товара",
        help_text="Опишите товар",
        validators=[
            custom_validator("превосходно", "роскошно"),
        ],
        default="Превосходно и роскошно",
    )

    is_on_main = models.BooleanField(
        "на главной",
        default=False,
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

    preview = models.ImageField(
        "превью",
        help_text="будет приведено к размеру 300x300",
        upload_to="catalog/preview",
        default="default.png",
    )

    updated = models.DateTimeField(
        "дата обновления",
        auto_now=True,
    )

    created = models.DateTimeField(
        "дата обновления",
        auto_now=True,
    )

    def get_image_300x300(self):
        return get_thumbnail(
            self.preview, "300x300", quality=51, crop="center"
        )

    def image_tmb(self):
        if self.preview:
            return mark_safe(f"<img src='{self.preview.url}' width='50'>")
        return "нет изображения"

    class Meta:
        verbose_name = "товар"
        verbose_name_plural = "товары"

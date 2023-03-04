from django.contrib import admin
from django.db import models

from catalog.models import Category, GalleryModel, Item, Tag
from tinymce.widgets import TinyMCE


class GalleryInline(admin.TabularInline):
    fk_name = "item"
    model = GalleryModel


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    inlines = [
        GalleryInline,
    ]
    exclude = ("canonical_name",)
    list_display = (
        Item.name.field.name,
        Item.is_published.field.name,
        "image_tmb",
    )
    list_editable = ("is_published",)
    list_display_links = ("name",)
    filter_horizontal = ("tags",)
    formfield_overrides = {models.TextField: {"widget": TinyMCE()}}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    exclude = ("canonical_name",)
    list_display = (
        Tag.slug.field.name,
        Tag.is_published.field.name,
    )
    list_editable = ("is_published",)
    list_display_links = ("slug",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ("canonical_name",)
    list_display = (
        Category.slug.field.name,
        Category.is_published.field.name,
    )
    list_editable = ("is_published",)
    list_display_links = ("slug",)

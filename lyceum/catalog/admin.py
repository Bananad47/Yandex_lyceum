from django.contrib import admin

from catalog.models import Category, Item, Tag


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        Item.name.field.name,
        Item.is_published.field.name,
    )
    list_editable = ("is_published",)
    list_display_links = ("name",)
    filter_horizontal = ("tags",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = (
        Tag.slug.field.name,
        Tag.is_published.field.name,
    )
    list_editable = ("is_published",)
    list_display_links = ("slug",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        Category.slug.field.name,
        Category.is_published.field.name,
    )
    list_editable = ("is_published",)
    list_display_links = ("slug",)

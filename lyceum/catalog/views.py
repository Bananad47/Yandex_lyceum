import datetime

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.db import models

from catalog.models import GalleryModel, Item


def item_list(request):
    template = "catalog/item_list.html"
    items = Item.objects.item_items_list()
    print([x.category.name for x in items])
    context = {"items": items}
    return render(request, template, context)


def item_detail(request, item_id):
    template = "catalog/item_main_page.html"
    queryset = Item.objects.item_items_list()
    item = get_object_or_404(queryset, pk=item_id)
    gallery = GalleryModel.objects.item_gallery(item_id)
    context = {"item": item, "gallery": gallery}
    return render(request, template, context)


def new_items(request):
    template = "catalog/new.html"
    items = (
            Item.objects.item_items_list()
            .filter(
                created__gte=datetime.date.today()-datetime.timedelta(days=7)
                )
            .order_by("?")
            )[:5]
    context = {
        "items": items
    }
    return render(request, template, context)


def friday_items(request):
    template = "catalog/friday.html"
    items = (
        Item.objects.item_items_list()
        .filter(
            updated__week_day=6
        )
        .order_by("updated")
    )[:5]

    context = {
        "items": items
    }
    return render(request, template, context)


def unverified(request):
    template = "catalog/unverified.html"
    items = (
        Item.objects.item_items_list()
        .filter(
            created__gte=models.F(
                Item.updated.field.name
            ) - datetime.timedelta(seconds=1),

            created__lte=models.F(
                    Item.updated.field.name
                ) + datetime.timedelta(seconds=1)
        )
        .order_by("?")
    )[:5]

    context = {
        "items": items
    }

    return render(request, template, context)


def regular(request, number):
    return HttpResponse(f"<body> {number} </body>")


def product_conventer_page(request, product_id):
    return HttpResponse(f"<body> id товара: {product_id}. </body>")

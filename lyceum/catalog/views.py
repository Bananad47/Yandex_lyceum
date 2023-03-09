from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Item


def item_list(request):
    template = "catalog/item_list.html"
    items = Item.objects.item_items_list()
    context = {"items": items}
    return render(request, template, context)


def item_detail(request, item_id):
    template = "catalog/item_main_page.html"
    item = Item.objects.item_detail(item_id)
    context = {"item": item[0]}
    return render(request, template, context)


def regular(request, number):
    return HttpResponse(f"<body> {number} </body>")


def product_conventer_page(request, product_id):
    return HttpResponse(f"<body> id товара: {product_id}. </body>")

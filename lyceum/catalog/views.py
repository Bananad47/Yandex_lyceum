from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from catalog.models import Item, GalleryModel


def item_list(request):
    template = "catalog/item_list.html"
    items = Item.objects.item_items_list()
    context = {"items": items}
    return render(request, template, context)


def item_detail(request, item_id):
    template = "catalog/item_main_page.html"
    queryset = Item.objects.item_items_list()
    item = get_object_or_404(queryset, pk=item_id)
    gallery = GalleryModel.objects.item_gallery(item_id)
    context = {
        "item": item,
        "gallery": gallery
        }
    return render(request, template, context)


def regular(request, number):
    return HttpResponse(f"<body> {number} </body>")


def product_conventer_page(request, product_id):
    return HttpResponse(f"<body> id товара: {product_id}. </body>")

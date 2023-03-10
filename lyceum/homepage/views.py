from django.shortcuts import render

from catalog.models import Item


def home(request):
    template = "homepage/home.html"
    items = Item.objects.item_homepage()
    context = {"items": items}
    return render(request, template, context)

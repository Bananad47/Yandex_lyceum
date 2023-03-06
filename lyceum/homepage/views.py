from django.shortcuts import render

from catalog.models import Item


def home(request):
    template = "homepage/home.html"
    context = {}
    return render(request, template, context)



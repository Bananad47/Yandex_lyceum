from django.http import HttpResponse


def item_list(request):
    return HttpResponse("<body>Список элементов</body>")


def item_detail(request, item_id):
    return HttpResponse(f"<body>Подробно элемент с id:{item_id}</body>")


def coffee(request):
    return HttpResponse("<body>Я чайник</body>", status=418)


def regular(request, number):
    return HttpResponse(f"<body>{number}</body>")


def product_conventer_page(request, product_id):
    return HttpResponse(f"<body>id товара: {product_id}.</body>")

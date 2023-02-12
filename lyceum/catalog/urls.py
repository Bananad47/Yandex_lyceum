from catalog import converters, views
from django.urls import path, re_path, register_converter

register_converter(converters.SixDigitProductIdConvecter, "id")

urlpatterns = [
    path("", views.item_list),
    path("<int:item_id>", views.item_detail),
    path("convector/<id:product_id>", views.product_conventer_page),
    re_path(r"^re/(?P<number>\d{2,}|[1-9])/", views.regular),
]

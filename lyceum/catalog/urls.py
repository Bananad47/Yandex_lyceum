from django.urls import path, re_path, register_converter

from catalog import converters, views


register_converter(converters.PositiveNumber, "id")

urlpatterns = [
    path("", views.item_list),
    path("<int:item_id>/", views.item_detail),
    path("convector/<id:product_id>/", views.product_conventer_page),
    re_path(r"^re/(?P<number>[1-9][0-9]+|[1-9])/$", views.regular),
]

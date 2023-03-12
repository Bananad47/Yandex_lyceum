from django.urls import path, re_path, register_converter

from catalog import converters, views

register_converter(converters.PositiveNumber, "id")

app_name = "catalog"

urlpatterns = [
    path("", views.item_list, name="item_list"),
    path("<int:item_id>/", views.item_detail, name="item_detail"),
    path("convector/<id:product_id>/", views.product_conventer_page),
    re_path(r"^re/(?P<number>[1-9][0-9]+|[1-9])/$", views.regular),
    path("new/", views.new_items),
    path("unverified", views.unverified)
]

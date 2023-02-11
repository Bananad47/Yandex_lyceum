import catalog.views
from django.urls import path


urlpatterns = [
    path("", catalog.views.item_list),
    path("<int:item_id>", catalog.views.item_detail),
]

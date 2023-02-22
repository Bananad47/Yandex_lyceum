from django.urls import path

from coffee import views

urlpatterns = [
    path("", views.coffee),
]

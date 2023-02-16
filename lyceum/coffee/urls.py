from coffee import views

from django.urls import path

urlpatterns = [
    path("", views.coffee),
]

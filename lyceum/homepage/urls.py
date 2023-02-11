from django.urls import path
import views  # это homepage views

urlpatterns = [
    path("", views.index),
]

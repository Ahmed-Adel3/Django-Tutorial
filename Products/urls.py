from django.urls import path
from . import views


urlpatterns = [
    path("", views.all_products, name="all_products"),
    path("<int:id>", views.product_details, name="details"),
    path("new", views.new, name="new"),
    path("edit/<int:id>", views.edit, name="edit"),
    path("delete/<int:id>", views.delete, name="delete")
]
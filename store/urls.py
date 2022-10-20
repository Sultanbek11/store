from django.urls import path, include
from .views import (
    list_stores,
    create_stores,
    create_product,
    detail_store
)

urlpatterns = [
    path('', list_stores),
    path('create/store/', create_stores),
    path('create/product/', create_product),
    path('detail/<int:id>', detail_store),
]

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StoreSerializer, ProductSerializer
from .models import Product, Store


@api_view(['GET'])
def list_stores(request):
    stores_list = Store.objects.all()
    serializer = StoreSerializer(stores_list, many=True)
    products_list = Product.objects.all()
    serializer_2 = ProductSerializer(products_list, many=True)
    return Response([serializer_2.data, serializer.data])


@api_view(['POST'])
def create_stores(request):
    serializer = StoreSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def detail_store(request, id):
    store_ = Store.objects.get(id=id)
    store_products_info = [
        {'id': product.id, 'title': product.title} for product in store_.products.all()
    ]
    store_info = {
        'id': store_.id,
        'title': store_.name_store,
        'store_products': store_products_info
    }

    # serializer = StoreSerializer(store_)
    # product_ = Product.objects.all().filter(store_id=id)
    # serializer_2 = ProductSerializer(product_)
    return Response(store_info)

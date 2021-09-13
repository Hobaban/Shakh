from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from product import models
from product.repositories import get_product, get_products, delete_product, update_product, create_product, \
    add_product_image
from product.serializers import ProductSerializer, ProductImageSerializer
from util.pagination import Paginator
from util.query import is_object_exist_409


@api_view(["GET"])
@permission_classes((AllowAny,))
def get_product_controller(request, pk):
    product = get_product(pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
@permission_classes((AllowAny,))
def update_product_controller(request, pk):
    serializer = ProductSerializer(data=request.data)
    serializer.is_valid()
    name = request.data["name"]
    update_product(pk, name=name)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["DELETE"])
@permission_classes((AllowAny,))
def remove_product_controller(request, pk):
    delete_product(pk)
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
@permission_classes((AllowAny,))
def get_products_controller(request):
    products = get_products()
    paginator = Paginator()
    context = paginator.paginate_queryset(products, request)
    serializer = ProductSerializer(context, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(["POST"])
@permission_classes((AllowAny,))
def add_product_controller(request):
    name = request.data["name"]
    is_object_exist_409(models.Product, name=name)
    product = create_product(name=name)
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
@permission_classes((AllowAny,))
def add_product_image_controller(request):
    product_id = request.data['product_id']
    image = request.data['image']
    product_image = add_product_image(product_id, image=image)
    serializer = ProductImageSerializer(product_image)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

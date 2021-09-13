from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from product import models
from product.repositories import get_product, get_products
from product.serializers import ProductSerializer, ProductImageSerializer
from util.pagination import Paginator
from util.query import is_object_exist_409


class ProductDetailView(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def get(request, pk):
        product = get_product(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @staticmethod
    def put(request, pk):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid()
        name = request.data["name"]
        product = get_product(pk)
        product.name = name
        product.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @staticmethod
    def delete(request, pk):
        product = get_product(pk)
        product.delete()
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductCreateListView(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def post(request):
        name = request.data["name"]
        is_object_exist_409(models.Product, name=name)
        product = models.Product()
        product.name = name
        product.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @staticmethod
    def get(request):
        products = get_products()
        paginator = Paginator()
        context = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(context, many=True)
        return paginator.get_paginated_response(serializer.data)


class ProductImage(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def post(request):
        product_id = request.data['product_id']
        file = request.data['image']
        product_image = models.ProductImage()
        product_image.product = get_object_or_404(models.Product, id=product_id)
        product_image.image = file
        product_image.image.name = file.name
        product_image.save()
        serializer = ProductImageSerializer(product_image)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

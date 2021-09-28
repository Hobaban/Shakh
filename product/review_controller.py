from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from product import models
from product.repositories import get_review, update_review, delete_review, create_review, add_review_image, \
    get_reviews_per_product, is_product_reviewed
from product.serializers import ReviewSerializer, ReviewImageSerializer
from util.pagination import Paginator
from util.query import is_object_exist_409


@api_view(["GET"])
@permission_classes((AllowAny,))
def get_review_controller(request, pk):
    review = get_review(pk)
    serializer = ReviewSerializer(review)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["PUT"])
@permission_classes((AllowAny,))
def update_review_controller(request, pk):
    serializer = ReviewSerializer(data=request.data)
    serializer.is_valid()
    context = request.data["context"]
    product_key = request.data["product_key"]
    reviewer_key = request.data["reviewer_key"]
    rate = request.data["rate"]
    title = request.data["title"]
    update_review(pk=pk, context=context, title=title, product_key=product_key, reviewer_key=reviewer_key, rate=rate)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["DELETE"])
@permission_classes((AllowAny,))
def remove_review_controller(request, pk):
    delete_review(pk)
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
@permission_classes((AllowAny,))
def get_reviews_controller(request):
    product_id = request.query_params.get('product_id')
    reviews = get_reviews_per_product(product_id=product_id)
    paginator = Paginator()
    context = paginator.paginate_queryset(reviews, request)
    serializer = ReviewSerializer(context, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(["POST"])
@permission_classes((AllowAny,))
def add_review_controller(request):
    title = request.data["title"]
    context = request.data["context"]
    product_key = request.data["product_key"]
    reviewer_key = request.data["reviewer_key"]
    is_product_reviewed(product_id=product_key, reviewer_id=reviewer_key)
    rate = request.data["rate"]
    review = create_review(context=context, title=title, product_key=product_key, reviewer_key=reviewer_key, rate=rate)
    serializer = ReviewSerializer(review)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["POST"])
@permission_classes((AllowAny,))
def add_review_image_controller(request):
    review_id = request.data['review_id']
    image = request.data['image']
    product_image = add_review_image(review_id, image=image)
    serializer = ReviewImageSerializer(product_image)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

from rest_framework import serializers

from account.serializers import UserSerializer
from product import models


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProductImage
        fields = ('image', 'product',)


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    product_images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = models.Product
        fields = ('id', 'name', 'product_images')


class ReviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReviewImage
        fields = ('image', 'review',)


class ReviewSerializer(serializers.HyperlinkedModelSerializer):
    review_images = ReviewImageSerializer(many=True, read_only=True)
    reviewer = UserSerializer()
    product = ProductSerializer()

    class Meta:
        model = models.Review
        fields = ('id', 'title', 'context', 'review_images', 'product', 'reviewer')

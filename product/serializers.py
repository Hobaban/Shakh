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
        fields = ('id', 'name', 'product_images', 'rate')


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
        fields = ('id', 'rate', 'title', 'context', 'review_images', 'reviewer', 'product')


class ReviewerStatSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    product = ProductSerializer()

    class Meta:
        model = models.Review
        fields = ('id', 'rate', 'product')


class UserStatSerializer(serializers.Serializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    class Meta:
        review_count = serializers.IntegerField()
        # review_list = ReviewSerializer(many=True)

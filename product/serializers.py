from rest_framework import serializers

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

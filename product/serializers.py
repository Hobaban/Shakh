from rest_framework import serializers

from product import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        name = serializers.CharField(required=True)
        model = models.Product
        fields = ('id', 'name')

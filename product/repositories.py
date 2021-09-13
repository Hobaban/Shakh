from django.http import Http404
from rest_framework.generics import get_object_or_404

from product import models
from product.models import Product, ProductImage


def add_product_image(product_id, image):
    product_image = ProductImage()
    product_image.product = get_object_or_404(models.Product, id=product_id)
    product_image.image = image
    product_image.image.name = image.name
    product_image.save()
    return product_image


def create_product(name):
    try:
        product = Product()
        product.name = name
        product.save()
        return Product
    except Exception as e:
        return e


def get_product(pk: int) -> Product:
    try:
        return Product.objects.get(pk=pk)

    except Product.DoesNotExist:
        raise Http404


def delete_product(pk) -> bool:
    try:
        product = get_product(pk)
        product.delete()
        product.save()
        return True
    except Exception as e:
        raise e


def update_product(pk, name) -> Product:
    try:
        product = get_product(pk)
        product.name = name
        product.save()
        return product
    except Product.DoesNotExist:
        raise Http404


def get_products() -> [Product]:
    try:
        return Product.objects.all().order_by('name')
    except Product.DoesNotExist:
        raise Http404


def get_product_images(product_key):
    product = get_product(product_key)
    images = ProductImage.objects.filter(product=product)
    return images

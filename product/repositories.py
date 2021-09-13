from django.http import Http404

from product.models import Product, ProductImage


def get_product(pk: int) -> Product:
    try:
        return Product.objects.get(pk=pk)

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

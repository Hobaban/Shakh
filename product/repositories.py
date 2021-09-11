from django.http import Http404

from product.models import Product


def get_product(pk):
    try:
        return Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        raise Http404


def get_products():
    try:
        return Product.objects.all()
    except Product.DoesNotExist:
        raise Http404

from django.http import Http404
from rest_framework.generics import get_object_or_404

from account.models import User
from product import models
from product.models import Product, ProductImage, ReviewImage, Review


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
        return product
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
        return Product.objects.all().order_by('created_date')
    except Product.DoesNotExist:
        raise Http404


def get_product_images(product_key):
    product = get_product(product_key)
    images = ProductImage.objects.filter(product=product)
    return images


def create_review(title: str, rate: float, context: str, product_key: int, reviewer_key: int) -> Review:
    try:
        review = Review()
        review.rate = rate
        review.context = context
        review.title = title
        review.product = get_product(product_key)
        review.reviewer = get_object_or_404(User, id=reviewer_key)
        review.save()
        return review
    except Exception as e:
        raise


def update_review(pk: int, title: str, rate: float, context: str, product_key: int, reviewer_key: int) -> Review:
    review = get_object_or_404(Review, id=pk)
    review.rate = rate
    review.context = context
    review.title = title
    review.product = get_product(product_key)
    review.reviewer = get_object_or_404(User, id=reviewer_key)
    review.save()
    return review


def get_reviews() -> [Review]:
    try:
        return Review.objects.all().order_by('title')
    except Review.DoesNotExist:
        raise Http404


def get_reviews_per_product(product_id):
    product = get_object_or_404(Product, id=product_id)
    return Review.objects.filter(product=product)


def get_review(pk) -> Review:
    try:
        return Review.objects.get(pk=pk)

    except Review.DoesNotExist:
        raise Http404


def delete_review(pk):
    try:
        review = get_review(pk)
        review.delete()
        return True
    except Exception as e:
        raise e


def add_review_image(review_id, image):
    review_image = ReviewImage()
    review_image.review = get_object_or_404(models.Review, id=review_id)
    review_image.image = image
    review_image.image.name = image.name
    review_image.save()
    return review_image

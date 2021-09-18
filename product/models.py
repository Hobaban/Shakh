from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from account.models import User


class Product(models.Model):
    name = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.CharField(max_length=250)
    rate = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    context = models.CharField(max_length=1024)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviewers')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_reviews', blank=True,
                                null=True)

    def __str__(self):
        return self.title


class ReviewImage(models.Model):
    review = models.ForeignKey(Review, related_name='review_images', on_delete=models.CASCADE, blank=True)
    image = models.ImageField(upload_to="media", blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.review.title


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='product_images', on_delete=models.CASCADE, blank=True)
    image = models.ImageField(upload_to="media", blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name

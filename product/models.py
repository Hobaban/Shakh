from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from account.models import User
from django_lifecycle import LifecycleModel, hook, AFTER_UPDATE, AFTER_CREATE


class Product(models.Model):
    name = models.CharField(max_length=250)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    rate = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)

    def __str__(self):
        return self.name


class Review(LifecycleModel):
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

    def calculate_product_average_rate(self):
        reviews = Review.objects.filter(product_id=self.product.id)
        reviewers_rate = 0
        reviewer_count = 0
        for review in reviews:
            reviewers_rate = review.rate + reviewers_rate
            reviewer_count = reviewer_count + 1
        rate = reviewers_rate / reviewer_count
        return rate

    @hook(AFTER_UPDATE)
    @hook(AFTER_CREATE)
    def on_publish(self):
        self.product.rate = self.calculate_product_average_rate()
        self.product.save()


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

from django.contrib import admin

from product.models import Product, ProductImage, Review, ReviewImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ('id', 'name', 'created_date', 'updated_date')
    list_filter = ('name', 'created_date', 'updated_date')


class ReviewImageInline(admin.TabularInline):
    model = ReviewImage
    extra = 3


class ProductReviews(admin.ModelAdmin):
    inlines = [ReviewImageInline]
    model = Review


admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ProductReviews)

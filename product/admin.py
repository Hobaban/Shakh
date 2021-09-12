from django.contrib import admin

from product.models import Product, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ]
    list_display = ('id', 'name', 'created_date', 'updated_date')
    list_filter = ('name', 'created_date', 'updated_date')


admin.site.register(Product, ProductAdmin)

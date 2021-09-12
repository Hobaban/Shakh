from django.urls import path
from product.views import ProductDetailView, ProductCreateListView, ProductImage

urlpatterns = [
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/', ProductCreateListView.as_view(), name='product-list'),
    path('products/images/', ProductImage.as_view(), name='product-images')
]

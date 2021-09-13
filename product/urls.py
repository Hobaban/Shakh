from django.urls import path

from product import views
from util.url import method_dispatch

urlpatterns = [
    path('products/', method_dispatch(POST=views.add_product_controller, GET=views.get_products_controller),
         name='product-list'),
    path('products/<int:pk>/',
         method_dispatch(GET=views.get_product_controller, PUT=views.update_product_controller,
                         DELETE=views.remove_product_controller),
         name='product-detail'),
    path('products/images/', method_dispatch(POST=views.add_product_image_controller), name='product-images')
]

from django.urls import path

from product import views
from product.review_controller import add_review_controller, get_reviews_controller, get_review_controller, \
    update_review_controller, remove_review_controller, add_review_image_controller
from util.url import method_dispatch

urlpatterns = [
    # products
    path('products/', method_dispatch(POST=views.add_product_controller, GET=views.get_products_controller),
         name='product-list'),
    path('products/<int:pk>/',
         method_dispatch(GET=views.get_product_controller, PUT=views.update_product_controller,
                         DELETE=views.remove_product_controller),
         name='product-detail'),
    path('products/images/', method_dispatch(POST=views.add_product_image_controller), name='product-images'),

    # reviews
    path('reviews/', method_dispatch(POST=add_review_controller, GET=get_reviews_controller),
         name='review-list'),
    path('reviews/<int:pk>/',
         method_dispatch(GET=get_review_controller, PUT=update_review_controller,
                         DELETE=remove_review_controller),
         name='review-detail'),
    path('reviews/images/', method_dispatch(POST=add_review_image_controller), name='review-images')

]

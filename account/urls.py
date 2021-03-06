# from decorator_include import decorator_include
from django.conf.urls import url
from django.urls import path
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny

from account import views

urlpatterns = [
    url(r'^send_code/$', views.send_otp_code_view, name='send_code'),
    url(r'^phone_login/$', views.phone_login_view, name='phone_login'),
    url(r'^forget_password/$', views.forget_password, name='forget_password'),
    url(r'^change_password/$', views.change_password, name='change_password'),
    url(r'^phone_register/$', views.phone_registration, name='phone_register'),
    url(r'^current_user/$', views.get_current_user, name='current_user'),
    url(r'^complete_profile/$', views.complete_profile, name='complete_profile'),
    url(r'^verify_phone/$', views.verify_token, name='verify_phone'),
    url(r'^hello/$', views.hello_world, name='hello_world')
    # decorator_include([api_view(["POST"]),permission_classes((AllowAny,))]
    # url(r'^email_login/$', views.email_login_view, name='login'),
    # url(r'^email_register/$', views.email_registration, name='email_register'),
]

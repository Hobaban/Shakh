# from decorator_include import decorator_include
from django.conf.urls import url
from django.urls import path
from rest_framework.decorators import permission_classes, api_view
from rest_framework.permissions import AllowAny

from account import views

urlpatterns = [
    url(r'^otp_login/$', views.otp_login_view, name='otp_login'),
    url(r'^email_login/$', views.email_login_view, name='login'),
    url(r'^send_code/$', views.send_otp_code_view, name='send_code'),
    url(r'^phone_register/$', views.phone_registration, name='phone_register'),
    url(r'^email_register/$', views.email_registration, name='email_register'),
    url(r'^current_user/$', views.get_current_user, name='current_user'),
    url(r'^hello/$', views.hello_world, name='hello_world')
    # decorator_include([api_view(["POST"]),permission_classes((AllowAny,))]
]

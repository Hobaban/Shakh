from account import models
from account.models import User
from rest_framework import status
from django.core.cache import cache
from account.util import generate_otp_code, check_otp_code, is_code_sent
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from account.services.service import get_tokens
from util.query import is_object_exist_409
from rest_framework.decorators import api_view, permission_classes
from account.serializers import LoginSerializer, EmailLoginSerializer, PhoneValidationSerializer, UserSerializer
from send_message.send_message import SMS


@api_view(["POST"])
@permission_classes((AllowAny,))
def email_login_view(request):
    EmailLoginSerializer(data=request.data).is_valid()
    email = str(request.data['email']).strip()
    password = str(request.data['password']).strip()
    user = get_object_or_404(models.User, email=email)
    if user.check_password(password):
        tokens = get_tokens(user)
        return Response({'tokens': tokens}, status=status.HTTP_201_CREATED)
    return Response({'tokens': "not valid"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(["POST"])
@permission_classes((AllowAny,))
def send_otp_code_view(request):
    PhoneValidationSerializer(data=request.data).is_valid()
    phone = request.data["phone"]
    otp_code = generate_otp_code()
    if not is_code_sent(phone):
        cache.set(phone, otp_code, timeout=1500)
        print(otp_code)
        if SMS().send_activation_code(phone, otp_code):
            return Response({'message': "code sent"}, status=status.HTTP_200_OK)
        return Response({'message': "code not sent"}, status=status.HTTP_409_CONFLICT)
    else:
        return Response({'message': "code is still valid"}, status=status.HTTP_409_CONFLICT)


@api_view(["POST"])
@permission_classes((AllowAny,))
def phone_login_view(request):
    LoginSerializer(data=request.data).is_valid()
    phone = str(request.data['phone']).strip()
    password = str(request.data['password']).strip()
    user = get_object_or_404(models.User, phone=phone)
    if user.check_password(password):
        tokens = get_tokens(user)
        return Response({'tokens': tokens}, status=status.HTTP_201_CREATED)
    return Response({'tokens': "not valid"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(["GET"])
@permission_classes((AllowAny,))
def hello_world(request):
    return Response({'message': "hello world!"}, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes((AllowAny,))
def phone_registration(request):
    phone = request.data['phone']
    password = request.data['password']
    otp_code = request.data['otp_code']
    is_object_exist_409(User, phone=phone)
    if check_otp_code(phone, otp_code):
        models.User.objects.create_user(username=phone, phone=phone, password=password,
                                        email="fake@" + phone + ".com")
        return Response({'message': "registered"}, status=status.HTTP_201_CREATED)
    return Response({'message': "wrong code"}, status=status.HTTP_403_FORBIDDEN)


@api_view(["POST"])
@permission_classes((AllowAny,))
def email_registration(request):
    email = request.data['email']
    password = request.data['password']
    is_object_exist_409(User, email=email)
    models.User.objects.create_user(username=email, password=password, phone=email, email=email)
    return Response({'message': "registered"}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_current_user(request):
    user = request.user
    user = get_object_or_404(User, id=user.id)
    serializer = UserSerializer(user)
    return Response(data=serializer.data, status=status.HTTP_200_OK)


def forget_password(request):
    email = request["email"]
    user = get_object_or_404(User, email=email)
    otp_code = generate_otp_code()
    if not is_code_sent(email):
        cache.set(email, otp_code, timeout=60)
        if SMS().send_forget_password(user.phone, user.phone, otp_code):
            return Response({'message': "code sent"}, status=status.HTTP_200_OK)
    return Response({'message': "code is still valid"}, status=status.HTTP_409_CONFLICT)

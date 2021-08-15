from django.core.cache import cache

from account.models import User
from account.util import get_time_difference
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens(user: User):
    refresh = RefreshToken.for_user(user)
    tokens = {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    return tokens


def set_user_otp_code(user: User, otp: int, ttl=60):
    return cache.set(user.phone, otp, timeout=ttl)


def get_current_user():
    pass

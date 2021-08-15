from rest_framework import status
from rest_framework.exceptions import APIException


class ObjectExistException(APIException):
    def __init__(self, message):
        self.status_code = status.HTTP_409_CONFLICT
        self.detail = message


class ValidationException(APIException):
    def __init__(self, message):
        self.status_code = status.HTTP_403_FORBIDDEN
        self.detail = message


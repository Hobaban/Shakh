from util.exceptions import ObjectExistException


def validate_data(klass_serializer, data: {}):
    serializer = klass_serializer(data=data)
    if serializer.is_valid():
        return True
    raise ObjectExistException(message=serializer.errors)

from util.exceptions import ObjectExistException


def get_or_none(model, *args, **kwargs):
    try:
        return model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        return None


def is_object_exist_409(model, *args, **kwargs):
    instance = get_or_none(model, *args, **kwargs)
    if instance:
        raise ObjectExistException(message=model().__class__.__name__ + "_Already_exist")

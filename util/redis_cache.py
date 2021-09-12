import json
import logging

from django.core.cache import cache


def get_cache_multiple_value(key, custom_value_name):
    if key:
        _json_value_data = cache.get(key)
        if _json_value_data is not None:
            __value = (json.loads(_json_value_data)).get(custom_value_name, None)
            return __value
    return None


def set_cache_multiple_value(key, value, custom_value_name, ttl=60):
    _json_value_data = cache.get(key)
    try:
        _exist_json = json.loads(_json_value_data)
        _dict_value = {custom_value_name: value}
        _dict_value.update(_exist_json)
        _json_data = json.dumps(_dict_value)
        _cache_status = cache.set(key, _json_data, ex=ttl)
        return _cache_status
    except Exception as error:
        logging.error(error)
        _json_data = json.dumps({custom_value_name: str(value)})
        _cache_status = cache.set(key, _json_data, ex=ttl)
        return _cache_status

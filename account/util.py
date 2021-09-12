import datetime
import json
import secrets

from django.core.cache import cache
from django.utils.timezone import utc

from util.redis_cache import get_cache_multiple_value


def check_otp_code(phone: int, otp_code: int, custom_value="otp_code") -> bool:
    code = get_cache_multiple_value(phone, custom_value)
    if code and code == str(otp_code):
        return True
    return False


def is_code_sent(phone, value_name: str):
    if get_cache_multiple_value(phone, value_name):
        return True
    return False


def get_time_difference(last_update_time):
    if last_update_time:
        now = datetime.datetime.now().replace(tzinfo=utc)
        time_difference = now - last_update_time
        return time_difference.total_seconds()


def generate_otp_code():
    return str(secrets.SystemRandom().randrange(999, 9999))


def get_cache_value(key, custom_value_name):
    json_value_data = cache.get(key)
    if json_value_data is not None:
        __value = (json.loads(json_value_data)).get(custom_value_name, None)
        return __value
    return None


def set_cache_multiple_value(key, value, custom_value_name, ttl=60):
    json_value = cache.get(key)
    try:
        exist_json = json.loads(json_value)
        dict_value = {custom_value_name: str(value)}
        dict_value.update(exist_json)
        json_data = json.dumps(dict_value)
        __cache_status = cache.set(str(key), json_data, timeout=ttl)
        return __cache_status
    except:
        json_data = json.dumps({custom_value_name: str(value)})
        __cache_status = cache.set(str(key), json_data, timeout=ttl)
        return __cache_status

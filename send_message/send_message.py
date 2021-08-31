import json
import logging
from kavenegar import *
from shakh.settings import sms
from django.core.cache import cache

sms_api_key = sms['sms_api_key']
user_api_key = sms['user_api_key']
secret_key = sms['secret_key']
sms_token_url = sms['sms_token_url']
sms_verification_url = sms['sms_verification_url']
sms_timeout = int(sms['sms_timeout'])


class SMS(object):
    def _get_token_from_api(self):
        try:
            data = {"UserApiKey": user_api_key,
                    "SecretKey": secret_key}
            r = requests.post(url=sms_token_url, data=data)
            token = r.json().get("TokenKey")
            return token
        except requests.exceptions as e:
            return e

    def get_token(self):
        token = cache.get("sms_token")
        if token:
            return token
        token = self._get_token_from_api()
        cache.set("sms_token", token, timeout=100)
        return token

    def send_activation_code(self, cell_number, activation_code):
        try:
            url = sms_verification_url
            token = self.get_token()
            payload = {"Code": activation_code, "MobileNumber": cell_number}
            headers = {
                'Content-Type': 'application/json',
                'x-sms-ir-secure-token': token
            }
            response = requests.request("POST", url, headers=headers, data=str(payload))
            if response.json().get("IsSuccessful"):
                return True
            return False
        except requests.exceptions as e:
            return e

import logging
from kavenegar import *
from shakh.settings import sms
from rest_framework import status
from rest_framework.exceptions import APIException as RestAPIException

sms_api_key = sms['sms_api_key']


class SMS(object):
    def __init__(self):
        self.api = KavenegarAPI(sms_api_key)

    def __send_sms(self, data):
        receptor = data.get("receptor")
        if receptor.startswith('0999'):
            data['receptor'] = '09210419379'
        if sms_api_key is None:
            raise RestAPIException(code=status.HTTP_400_BAD_REQUEST, detail="MISSING_REQUIRED_FIELD")
        try:
            params = data
            response = self.api.verify_lookup(params)
        except (APIException, HTTPException) as e:
            logging.error(e.args[0].decode('utf8'))
            return False
        return True

    def send_activation_code(self, cell_number, activation_code):
        data = {'receptor': cell_number,
                'token': activation_code,
                'type': 'sms',
                'template': 'x'}
        return self.__send_sms(data)

    def send_forget_password(self, cell_number, username, password):
        data = {'receptor': cell_number,
                'token': password,
                'token2': password,
                'type': 'sms',
                'template': 'x'}
        return self.__send_sms(data)

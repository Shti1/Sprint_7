import requests

from data import Url, DataForAuth


class AuthMethods:
    @staticmethod
    def create_auth():
        response = requests.post(f'{Url.BASE_URL}{Url.LOGIN_COURIER_URL}', json=DataForAuth.CREATE_AUTH_BODY)
        return response.json()['id']
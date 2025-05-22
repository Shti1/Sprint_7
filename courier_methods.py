import pytest
import requests

from data import Url


class CourierMethods:
    @staticmethod
    def create_courier(body):
        return requests.post(f'{Url.BASE_URL}{Url.CREATE_COURIER_URL}', json=body)

    @staticmethod
    def delete_courier(courier_id):
        return requests.delete(f'{Url.BASE_URL}{Url.DELETE_COURIER_URL.format(courier_id=courier_id)}')

    @staticmethod
    def login_courier(login=None, password=None, payload=None, timeout=10):
        """
        Авторизация курьера с таймаутом
        """
        if payload is None:
            payload = {
                "login": login,
                "password": password
            }
        try:
            return requests.post(
                f'{Url.BASE_URL}{Url.LOGIN_COURIER_URL}',
                json=payload,
                timeout=timeout
            )
        except requests.exceptions.RequestException as e:
            pytest.fail(f"Ошибка соединения: {str(e)}")

    @staticmethod
    def get_courier_id(login, password):
        response = CourierMethods.login_courier(login, password)
        if response.status_code == 200:
            return response.json().get('id')
        return None
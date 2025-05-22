import requests
from data import Url

class OrderMethods:
    @staticmethod
    def create_order(order_data):
        """Создание нового заказа"""
        return requests.post(
            f'{Url.BASE_URL}{Url.CREATE_ORDER_URL}',
            json=order_data
        )

    @staticmethod
    def cancel_order(track):
        return requests.put(
            f'{Url.BASE_URL}{Url.CANCEL_ORDER_URL}',
            json={'track': track}
        )

    @staticmethod
    def get_order_id_by_track(track):
        """Получение ID заказа по трек-номеру"""
        response = OrderMethods.get_order_by_track(track)
        if response.status_code == 200:
            return response.json()["order"]["id"]
        return None

    @staticmethod
    def accept_order(courier_id, order_id):
        """Принятие заказа курьером"""
        return requests.put(
            f'{Url.BASE_URL}{Url.ACCEPT_ORDER_URL.format(order_id=order_id)}',
            params={"courierId": courier_id} if courier_id else None
        )

    @staticmethod
    def get_order_by_track(track):
        """Получение заказа по трек-номеру"""
        return requests.get(
            f'{Url.BASE_URL}{Url.TRACK_ORDER_URL}',
            params={"t": track} if track else None
        )

    @staticmethod
    def get_orders_list():
        """Получение списка заказов без параметров"""
        return requests.get(f'{Url.BASE_URL}{Url.GET_ORDERS_URL}')
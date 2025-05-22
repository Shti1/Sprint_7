from pyclbr import Class


class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    #Создание курьера
    CREATE_COURIER_URL = '/api/v1/courier'
    #Логин курьера
    LOGIN_COURIER_URL = '/api/v1/courier/login'
    #Создание заказа
    CREATE_ORDER_URL = '/api/v1/orders'
    #Список заказов
    GET_ORDERS_URL = '/api/v1/orders'
    #Отменить заказ
    CANCEL_ORDER_URL = '/api/v1/orders/cancel'

    #Дополнительно

    #Удалить курьера
    DELETE_COURIER_URL = '/api/v1/courier/{courier_id}'
    #Принять заказ
    ACCEPT_ORDER_URL = '/api/v1/orders/accept/{order_id}'
    #Получить заказ по его номеру
    TRACK_ORDER_URL = '/api/v1/orders/track'

class DataForOrder:
    CREATE_ORDER_BODY = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": [
        "BLACK"
        ]
    }

class DataForAuth:
    CREATE_AUTH_BODY = {
    "login": "ninja",
    "password": "1234"
    }
import random

from faker import Faker

fake = Faker()


def generate_order_data(color=None):
    """Генерирует данные для создания заказа"""
    data = {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.address(),
        "metroStation": random.randint(1, 30),
        "phone": fake.phone_number(),
        "rentTime": random.randint(1, 7),
        "deliveryDate": fake.date_between(start_date='today', end_date='+7d').isoformat(),
        "comment": fake.sentence()
    }

    if color is not None:
        data["color"] = color if isinstance(color, list) else [color]

    return data

def generate_courier_body():
    login = f"{fake.user_name()}_{fake.random_int(min=100, max=999)}"
    return {
        "login": login,
        "password": fake.password(),
        "firstName": fake.first_name()
    }
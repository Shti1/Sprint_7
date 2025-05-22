import pytest
from courier_methods import CourierMethods
from generators import generate_courier_body, generate_order_data
from order_methods import OrderMethods

@pytest.fixture
def new_courier():
    """Фикстура для создания и удаления тестового курьера"""
    courier_data = generate_courier_body()
    response = CourierMethods.create_courier(courier_data)
    courier_id = CourierMethods.get_courier_id(
        courier_data['login'],
        courier_data['password']
    )
    yield courier_data, courier_id, response  # Добавляем response для проверок
    if courier_id:
        CourierMethods.delete_courier(courier_id)

@pytest.fixture
def temp_courier():
    """Фикстура для временного курьера (для тестов дубликатов)"""
    courier_data = generate_courier_body()
    response = CourierMethods.create_courier(courier_data)
    courier_id = CourierMethods.get_courier_id(
        courier_data['login'],
        courier_data['password']
    )
    yield courier_data
    if courier_id:
        CourierMethods.delete_courier(courier_id)

@pytest.fixture
def invalid_courier_data(request):
    """Фикстура для генерации данных курьера без обязательного поля"""
    missing_field = request.param  # Получаем параметр из parametrize
    courier_data = generate_courier_body()
    del courier_data[missing_field]
    return courier_data

@pytest.fixture
def order_data(request):
    """Генерация данных заказа с параметризацией цвета"""
    color = getattr(request, 'param', None)
    return generate_order_data(color=color)

@pytest.fixture
def created_order(order_data):
    """Создание и отмена тестового заказа"""
    response = OrderMethods.create_order(order_data)
    order_track = response.json()["track"]
    yield order_track, response  # Добавляем response для проверок
    OrderMethods.cancel_order(order_track)
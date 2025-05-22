import allure
from order_methods import OrderMethods


class TestGetOrdersList:
    @allure.title("TC-1. Получение списка заказов без фильтрации")
    def test_get_orders_list_basic(self):
        """
        Проверяет базовый сценарий получения списка заказов:
        - возвращается код 200
        - в ответе есть непустой список заказов
        - каждый заказ содержит обязательные поля
        """
        with allure.step('1. Отправить запрос на получение списка заказов'):
            response = OrderMethods.get_orders_list()

        with allure.step('2. Проверить ответ сервера'):
            assert response.status_code == 200, (
                f"Ожидался код 200, получен {response.status_code}"
            )

            response_data = response.json()
            assert "orders" in response_data, "В ответе отсутствует ключ 'orders'"
            assert isinstance(response_data["orders"], list), "'orders' должен быть списком"
            assert len(response_data["orders"]) > 0, "Список заказов не должен быть пустым"

        with allure.step('3. Проверить структуру заказов'):
            required_fields = [
                "id", "firstName", "lastName", "address",
                "metroStation", "phone", "rentTime",
                "deliveryDate", "track", "status"
            ]

            for order in response_data["orders"]:
                for field in required_fields:
                    assert field in order, f"В заказе отсутствует обязательное поле {field}"
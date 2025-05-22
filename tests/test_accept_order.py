import allure
import pytest
from order_methods import OrderMethods


class TestAcceptOrder:
    @allure.title("TC-1. Успешное принятие заказа")
    def test_successful_order_accept(self, new_courier, created_order):
        """Проверка успешного принятия заказа"""
        _, courier_id, _ = new_courier
        order_track, _ = created_order

        with allure.step("Получить ID заказа по треку"):
            order_id = OrderMethods.get_order_id_by_track(order_track)

        with allure.step("Принять заказ"):
            response = OrderMethods.accept_order(courier_id, order_id)

        with allure.step("Проверить ответ"):
            assert response.status_code == 200
            assert response.json() == {"ok": True}

    @allure.title("TC-2. Ошибка при отсутствии ID курьера")
    def test_missing_courier_id(self, created_order):
        """Проверка обработки отсутствия ID курьера"""
        order_track, _ = created_order
        order_id = OrderMethods.get_order_id_by_track(order_track)

        response = OrderMethods.accept_order(None, order_id)
        assert response.status_code == 400
        assert "Недостаточно данных" in response.json().get("message", "")

    @allure.title("TC-3. Ошибка при неверном ID курьера")
    def test_invalid_courier_id(self, created_order):
        """Проверка несуществующего ID курьера"""
        order_track, _ = created_order
        order_id = OrderMethods.get_order_id_by_track(order_track)

        response = OrderMethods.accept_order("invalid_id", order_id)
        assert response.status_code == 404
        assert "Курьер не найден" in response.json().get("message", "")

    @allure.title("TC-4. Ошибка при отсутствии ID заказа")
    def test_missing_order_id(self, new_courier):
        """Проверка обработки отсутствия ID заказа"""
        _, courier_id, _ = new_courier

        response = OrderMethods.accept_order(courier_id, None)
        assert response.status_code == 400
        assert "Недостаточно данных" in response.json().get("message", "")

    @allure.title("TC-5. Ошибка при неверном ID заказа")
    def test_invalid_order_id(self, new_courier):
        """Проверка несуществующего ID заказа"""
        _, courier_id, _ = new_courier

        response = OrderMethods.accept_order(courier_id, "invalid_order")
        assert response.status_code == 404
        assert "Заказ не найден" in response.json().get("message", "")
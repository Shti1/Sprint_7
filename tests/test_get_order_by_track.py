import allure
import pytest
from order_methods import OrderMethods


class TestGetOrderByTrack:
    @allure.title("TC-1. Успешное получение заказа по треку")
    def test_successful_order_get(self, created_order):
        """Проверка успешного получения заказа"""
        order_track, _ = created_order

        with allure.step("Получить заказ по треку"):
            response = OrderMethods.get_order_by_track(order_track)

        with allure.step("Проверить ответ"):
            assert response.status_code == 200
            assert "order" in response.json()
            assert response.json()["order"]["track"] == order_track

    @allure.title("TC-2. Ошибка при отсутствии трека")
    def test_missing_track(self):
        """Проверка обработки отсутствия трека"""
        response = OrderMethods.get_order_by_track(None)
        assert response.status_code == 400
        assert "Недостаточно данных" in response.json().get("message", "")

    @allure.title("TC-3. Ошибка при несуществующем треке")
    def test_nonexistent_track(self):
        """Проверка несуществующего трека"""
        response = OrderMethods.get_order_by_track(999999)
        assert response.status_code == 404
        assert "Заказ не найден" in response.json().get("message", "")
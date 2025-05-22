import allure
import pytest

from courier_methods import CourierMethods


class TestDeleteCourier:
    @allure.title("Успешное удаление курьера")
    def test_success_delete_courier(self, new_courier):
        """Тест успешного удаления курьера"""
        courier_data, courier_id, _ = new_courier  # Распаковываем все 3 значения

        with allure.step("Отправить запрос на удаление"):
            response = CourierMethods.delete_courier(courier_id)

        with allure.step("Проверить ответ"):
            assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
            assert response.json() == {"ok": True}, "Тело ответа не соответствует ожидаемому"

    @allure.title("Попытка удаления несуществующего курьера")
    @pytest.mark.parametrize("invalid_id", ["999999", "0", "abc", None])
    def test_delete_nonexistent_courier(self, invalid_id):
        with allure.step(f"Отправить запрос с невалидным ID: {invalid_id}"):
            response = CourierMethods.delete_courier(invalid_id)

        with allure.step("Проверить ошибку"):
            assert response.status_code == 404
            assert "message" in response.json()

    @allure.title("Попытка удаления без указания ID")
    def test_delete_without_id(self):
        with allure.step("Отправить запрос без ID"):
            # В вашем случае метод delete_courier требует ID, поэтому тестируем через requests
            import requests
            from data import Url
            response = requests.delete(f"{Url.BASE_URL}{Url.DELETE_COURIER_URL.format(courier_id='')}")

        with allure.step("Проверить ошибку"):
            assert response.status_code == 400
            assert response.json()["message"] == "Недостаточно данных для удаления курьера"


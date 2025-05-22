import allure
import pytest


class TestCreateOrder:
    @allure.title("TC-1. Создание заказа с разными вариантами цветов")
    @pytest.mark.parametrize("order_data", [
        None,  # Без цвета
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"]
    ], indirect=True)
    def test_create_order_with_colors(self, created_order):
        """
        Проверяет создание заказа с разными вариантами цветов:
        - без цвета
        - только BLACK
        - только GREY
        - оба цвета
        """
        track, response = created_order  # Получаем и track и response из фикстуры

        with allure.step("Проверить ответ сервера"):
            assert response.status_code == 201, f"Ожидался код 201, получен {response.status_code}"

            response_data = response.json()
            assert "track" in response_data, "В ответе отсутствует track-номер"
            assert isinstance(response_data["track"], int), "Track должен быть числом"
            assert response_data["track"] > 0, "Track должен быть положительным числом"

        with allure.step("Проверить валидность track-номера"):
            assert isinstance(track, int), "Track должен быть числом"
            assert track > 0, "Track должен быть положительным"
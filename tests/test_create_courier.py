import allure
import pytest

from courier_methods import CourierMethods


class TestCreateCourier:
    @allure.title('TC-1. Успешное создание курьера')
    def test_courier_creation(self, new_courier):
        """
        Проверяет:
        - Код ответа 201 при создании
        - Тело ответа {"ok": true}
        - Наличие courier_id в данных
        """
        courier_data, courier_id, response = new_courier

        with allure.step('Проверить ответ сервера'):
            assert response.status_code == 201
            assert response.json() == {"ok": True}
            assert courier_id is not None  # Проверка что ID был получен

    @allure.title('TC-2. Запрет создания дубликата курьера')
    def test_duplicate_courier_creation(self, temp_courier):
        """
        Проверяет:
        - Код ошибки 409 при дубликате
        - Сообщение о занятом логине
        """
        with allure.step('Попытаться создать дубликат'):
            duplicate_response = CourierMethods.create_courier(temp_courier)

        with allure.step('Проверить ошибку'):
            assert duplicate_response.status_code == 409
            assert duplicate_response.json().get("message") == "Этот логин уже используется"

    @allure.title("TC-3. Проверка обязательных полей")
    @pytest.mark.parametrize("invalid_courier_data", ["login", "password", "firstName"], indirect=True)
    def test_courier_required_fields(self, invalid_courier_data):
        """
        Проверяет:
        - Код ошибки 400 при отсутствии обязательного поля
        - Сообщение о недостающих данных
        """
        with allure.step('Отправить запрос с неполными данными'):
            response = CourierMethods.create_courier(invalid_courier_data)

        with allure.step('Проверить ответ сервера'):
            assert response.status_code == 400, "Ожидался статус код 400"
            assert "Недостаточно данных для создания учетной записи" in response.json().get("message", "")
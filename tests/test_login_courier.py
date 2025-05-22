import time

import allure
import pytest


from courier_methods import CourierMethods


class TestLoginCourier:
    @allure.title("TC-1. Успешная авторизация курьера")
    def test_successful_courier_login(self, new_courier):
        """Проверка успешной авторизации созданного курьера"""
        courier_data, courier_id, _ = new_courier

        with allure.step('Выполнить авторизацию'):
            login_response = CourierMethods.login_courier(
                login=courier_data['login'],
                password=courier_data['password']
            )

        with allure.step('Проверить ответ сервера'):
            assert login_response.status_code == 200, "Ожидался код 200"
            assert 'id' in login_response.json(), "В ответе отсутствует ID"
            assert login_response.json()['id'] == courier_id, "ID не совпадает"

    @allure.title("TC-2. Проверка обязательных полей при авторизации")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_required_fields(self, new_courier, missing_field):
        """Проверка отсутствия обязательных полей"""
        courier_data, _, _ = new_courier

        with allure.step(f'Подготовить данные без поля "{missing_field}"'):
            auth_data = {
                "login": courier_data["login"],
                "password": courier_data["password"]
            }
            del auth_data[missing_field]

        with allure.step('Отправить запрос на авторизацию'):
            response = CourierMethods.login_courier(**auth_data)

        with allure.step('Проверить ошибку'):
            assert response.status_code == 400, "Ожидался код 400"
            assert "Недостаточно данных для входа" in response.json().get("message", "")

    @allure.title("TC-3. Ошибка при неверных учетных данных")
    @pytest.mark.parametrize("wrong_field", ["login", "password"])
    def test_wrong_credentials(self, new_courier, wrong_field):
        """Проверка неверных учетных данных"""
        courier_data, _, _ = new_courier

        with allure.step('Подготовить неверные данные'):
            credentials = {
                "login": courier_data["login"],
                "password": courier_data["password"]
            }
            credentials[wrong_field] = "wrong_" + credentials[wrong_field]

        with allure.step('Отправить запрос с неверными данными'):
            response = CourierMethods.login_courier(**credentials)

        with allure.step('Проверить ошибку'):
            assert response.status_code == 404, "Ожидался код 404"
            assert "Учетная запись не найдена" in response.json().get("message", "")

    @allure.title("TC-4. Авторизация несуществующего курьера")
    def test_nonexistent_courier_login(self):
        """Проверка авторизации несуществующего пользователя"""
        with allure.step('Подготовить случайные данные'):
            test_data = {
                "login": f"nonexistent_{time.time()}",
                "password": "invalid_password_123"
            }

        with allure.step('Отправить запрос на авторизацию'):
            response = CourierMethods.login_courier(**test_data)

        with allure.step('Проверить ошибку'):
            assert response.status_code == 404, "Ожидался код 404"
            assert response.json().get("message") == "Учетная запись не найдена"
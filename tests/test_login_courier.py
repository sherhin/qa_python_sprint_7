import allure

from helpers import Helpers as help
from conftest import api_client
from data import Endpoints, HttpMethods, ResponseTexts


class TestLoginCourier:

    @allure.title('Тест авторизации курьера')
    def test_login_courier(self, api_client):
        data = help.generate_courier_data()
        help.create_courier(api_client, data)
        response = api_client.send_request(HttpMethods.post, Endpoints.LOGIN, data)
        courier_id = response.json()['id']
        response_texts = ResponseTexts()
        response_texts.courier_login = courier_id
        formated_response = help.formate_response(response.status_code, response.text)
        assert formated_response == response_texts.courier_login

    @allure.title('Тест авторизации курьера без логина')
    def test_login_courier_without_login_negative(self, api_client):
        data = help.generate_courier_data()
        help.create_courier(api_client, data)
        data['login'] = None
        response = api_client.send_request(HttpMethods.post, Endpoints.LOGIN, data)
        formated_response = help.formate_response(response.status_code, response.text)
        assert formated_response == ResponseTexts.without_required_fields_login

    @allure.title('Тест авторизации курьера без пароля')
    def test_login_courier_without_password_negative(self, api_client):
        data = help.generate_courier_data()
        help.create_courier(api_client, data)
        data['password'] = None
        response = api_client.send_request(HttpMethods.post, Endpoints.LOGIN, data)
        formated_response = help.formate_response(response.status_code, response.text)
        assert formated_response == ResponseTexts.without_required_fields_password

    @allure.title('Тест авторизации курьера с несуществующими данными')
    def test_login_courier_user_not_exists_negative(self, api_client):
        data = {
            'login': 'fakelogin',
            'password': 'fakepassword',
        }
        response = api_client.send_request(HttpMethods.post, Endpoints.LOGIN, data)
        formated_response = help.formate_response(response.status_code, response.text)
        assert formated_response == ResponseTexts.courier_not_exists

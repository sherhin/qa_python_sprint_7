import allure
import pytest

from  helpers import Helpers as help
from conftest import api_client
from data import Endpoints, HttpMethods, ResponseTexts

class TestCreateCourier:
    @allure.title('Тест создания курьера')
    def test_create_courier(self, api_client):
        data = help.generate_courier_data()
        response = api_client.send_request(HttpMethods.post, Endpoints.COURIER, data)
        formated_response = help.formate_response(response.status_code, response.text)
        assert formated_response == ResponseTexts.courier_created

    @allure.title('Тест создания курьера с данными уже существующего')
    def test_create_courier_exists_negative(self, api_client):
        data = help.generate_courier_data()
        api_client.send_request(HttpMethods.post, Endpoints.COURIER, data)
        second_response = api_client.send_request(HttpMethods.post, Endpoints.COURIER, data)
        formated_response = help.formate_response(second_response.status_code, second_response.text)
        assert formated_response == ResponseTexts.courier_exists

    @allure.title('Тест создания курьера без обязательных полей')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_create_courier_without_req_fields_negative(self, api_client, field):
        data = help.generate_courier_data()
        if data.get(field):
            data[field] = None
        response = api_client.send_request(HttpMethods.post, Endpoints.COURIER, data)
        formated_response = help.formate_response(response.status_code, response.text)
        assert formated_response == ResponseTexts.without_required_fields



import allure
import pytest

from helpers import Helpers as help
from data import HttpMethods, Endpoints, ResponseTexts
from conftest import api_client


class TestCreateOrder:

    @allure.title('Тест создания заказов')
    @pytest.mark.parametrize('color', [[], ['Black'], ['Grey'], ['Black', 'Grey']])
    def test_create_order(self, api_client, color):
        data = help.generate_order_data()
        data['color'] = color
        response = api_client.send_request(HttpMethods.post, Endpoints.ORDER, data)
        order_id = response.json()['track']
        response_texts = ResponseTexts()
        response_texts.order_create = order_id
        formated_response = help.formate_response(response.status_code, response.text)
        assert formated_response == response_texts.order_create


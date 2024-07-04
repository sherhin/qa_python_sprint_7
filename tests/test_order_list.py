import allure

from helpers import Helpers as help
from data import HttpMethods, Endpoints


class TestOrderList:

    @allure.title('Тест получения списка заказов')
    def test_get_order_list(self, api_client):
        data = help.generate_order_data()
        help.create_order(api_client, data)
        response = api_client.send_request(HttpMethods.get, Endpoints.ORDER)
        orders = response.json()['orders']
        assert len(orders) > 0


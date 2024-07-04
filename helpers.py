from faker import Faker
from conftest import api_client
from data import HttpMethods, Endpoints


class Helpers:

    @staticmethod
    def generate_courier_data():
        fake = Faker()
        random_login = fake.user_name()
        random_password = fake.password(
            length=12, special_chars=True, digits=True, upper_case=True, lower_case=True
        )
        random_first_name = fake.first_name_male()
        data = {
            'login': random_login,
            'password': random_password,
            'first_name': random_first_name
        }
        return data

    @staticmethod
    def generate_order_data():
        fake = Faker('ru_RU')
        data = {
            "firstName": fake.first_name(),
            "lastName": fake.last_name(),
            "address": fake.street_address(),
            "metroStation": fake.text(max_nb_chars=7),
            "phone": fake.phone_number(),
            "rentTime": fake.random_int(min=1, max=10),
            "deliveryDate": fake.date_this_decade().strftime('%Y-%m-%d'),
            "comment": fake.text(),
            "color": None
        }
        return data

    @staticmethod
    def formate_response(status_code, message):
        format_response = [status_code, message]
        return format_response

    @staticmethod
    def create_courier(api_client, data):
        courier = api_client.send_request(HttpMethods.post, Endpoints.COURIER, data)
        return courier

    @staticmethod
    def create_order(api_client, data):
        order = api_client.send_request(HttpMethods.post, Endpoints.ORDER, data)
        return order

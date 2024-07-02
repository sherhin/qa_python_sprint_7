
class Endpoints:
    BASE = 'https://qa-scooter.praktikum-services.ru/'
    LOGIN = 'api/v1/courier/login'
    COURIER = 'api/v1/courier/'
    ORDER = 'api/v1/orders'
    ACCEPT_ORDER = 'api/v1/accept'
    TRACK_ORDER = 'api/v1/orders/track'


class HttpMethods:
    get = 'GET'
    post = 'POST'
    put = 'PUT'
    delete = 'DELETE'


class ResponseTexts:
    courier_created = [201, '{"ok":true}']
    courier_exists = [409, '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}']
    without_required_fields = [400, '{"code":400,"message":"Недостаточно данных для создания учетной записи"}']
    without_required_fields_login = [400, '{"code":400,"message":"Недостаточно данных для входа"}']
    without_required_fields_password = [504, 'Service unavailable']
    courier_not_exists = [404, '{"code":404,"message":"Учетная запись не найдена"}']

    @property
    def courier_login(self):
        return [200, f'{{"id":{self._courier_id}}}']

    @courier_login.setter
    def courier_login(self, value):
        self._courier_id = value

    @property
    def order_create(self):
        return [201, f'{{"track":{self._order_id}}}']

    @order_create.setter
    def order_create(self, value):
        self._order_id = value

import allure
import requests

from src.helpers.logger import log

BASE_URL = 'https://demowebshop.tricentis.com'
LOGIN = 'Ivanov.V@mail.ru'
PASSWORD = 'qwerty123'


@allure.step("Получение cookie авторизации через API")
def get_cookies():
    url = BASE_URL + "/login"
    data = {"Email": LOGIN,
            "Password": PASSWORD,
            "RememberMe": False}
    response = requests.post(url=url,
                                 data=data,
                                 allow_redirects=False)
    log(response=response, request_body=data)
    return response.cookies


@allure.step("Добавление продукта {product_id} в количестве {quantity} в корзину через API")
def add_product_in_cart(product_id, quantity=1):
    url = BASE_URL + f'/addproducttocart/details/{product_id}/1'
    data = {f'addtocart_{product_id}.EnteredQuantity': quantity}
    response = requests.post(url=url, data=data, allow_redirects=False)
    log(response=response, request_body=data, allure_logging=True)
    return response

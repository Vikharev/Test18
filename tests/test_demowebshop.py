import allure
from allure_commons._allure import step
from selene import browser, have, be

from src.api import demowebshop_api

BASE_URL = "https://demowebshop.tricentis.com/"

@allure.epic("Разработка интернет-магазина")
@allure.feature("Функционал обработки товаров в корзине")
@allure.story("Добавление товаров в корзину")
@allure.title("Добавление одного товара в корзину")
def test_add_to_cart_one_product():
    response = demowebshop_api.add_product_in_cart(13)

    with step("Открытие браузера"):
        browser.open(BASE_URL)
        browser.driver.add_cookie({"name": "Nop.customer",
                                   "value": response.cookies.get("Nop.customer")})
        browser.open(BASE_URL)

    with step("Открытие каталога книг"):
        browser.open(BASE_URL + "books")

    with step("Проверка количества товаров в header"):
        browser.element(".cart-qty").should(have.text('1'))

    with step("Открытие корзины"):
        browser.open(BASE_URL + "cart")

    with step("Проверка количества товаров в корзине"):
        browser.element(".cart-qty").should(have.text('1'))
        browser.all(".cart-item-row").should(have.size(1))

    with step("Проверка содержимого корзины"):
        browser.element(".product-name").should(have.text('Computing and Internet'))
        browser.element(".product-subtotal").should(have.text('10.00'))


@allure.epic("Разработка интернет-магазина")
@allure.feature("Функционал обработки товаров в корзине")
@allure.story("Добавление товаров в корзину")
@allure.title("Покупка нескольких позиций одного товара")
def test_add_to_cart_few_products():
    response = demowebshop_api.add_product_in_cart(31, 3)

    with step("Открытие браузера"):
        browser.open(BASE_URL)
        browser.driver.add_cookie({"name": "Nop.customer",
                                   "value": response.cookies.get("Nop.customer")})
        browser.open(BASE_URL)

    with step("Открытие каталога ноутбуков"):
        browser.open(BASE_URL + "notebooks")

    with step("Проверка, что в хедере отображается количество товаров, что находятся в корзине"):
        browser.element(".cart-qty").should(have.text('3'))

    with step("Открытие корзины"):
        browser.open(BASE_URL + "/cart")

    with step("Проверка количества товаров в самой корзине и в хедере"):
        browser.element(".cart-qty").should(have.text('3'))
        browser.all(".cart-item-row").should(have.size(1))

    with step("Проверка содержимого корзины"):
        browser.element(".product-name").should(have.text('14.1-inch Laptop'))
        browser.element(".product-subtotal").should(have.text('4770.00'))
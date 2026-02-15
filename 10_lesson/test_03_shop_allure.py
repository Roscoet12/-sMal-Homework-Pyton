from selenium import webdriver
import allure

from shop.Main import Main
from shop.Catalog import Catalog
from shop.Cart import Cart
from shop.Order import Order

@allure.title('Цена в корзине совпадает с ожидаемой ценой')
@allure.description('Тест проверяет, что после входа в личный кабинет '
                    'добавления определенных товаров'
                    'и ввода данных для доставки,'
                    f'цена в корзине совпадет с ожидаемой. ')
@allure.feature('BASKET')
@allure.severity('CRITICAL')
def test_test_shop_checkout_total():
    options = webdriver.FirefoxOptions()
    browser = webdriver.Firefox(options=options)

    main_page = Main(browser)

    main_page.get_browser()
    main_page.autorization('standard_user', 'secret_sauce')

    catalog_page = Catalog(browser)
    catalog_page.adding_product_to_cart()
    catalog_page.cart()

    cart_page = Cart(browser)
    cart_page.user_data('Kseniya', 'Malysheva', 195299)

    order_page = Order(browser)
    order_page.price()

    expected_price = '$58.29'
    with allure.step(f'Проверить, что фактическая цена совпала с {expected_price}'):
        assert expected_price == order_page.price()

    with allure.step('Закрыть браузер'):
        browser.quit()
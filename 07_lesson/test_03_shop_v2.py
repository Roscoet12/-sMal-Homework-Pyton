from selenium import webdriver

from shop.Main import Main
from shop.Catalog import Catalog
from shop.Cart import Cart
from shop.Order import Order


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
    cart_page.user_data('Kseniya', 'Malysheva', '195299')

    order_page = Order(browser)
    order_page.price()
    expected_price = '$58.29'

    assert expected_price == order_page.price()

    browser.quit()

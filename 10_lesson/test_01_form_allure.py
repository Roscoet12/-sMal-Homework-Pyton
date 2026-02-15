from selenium import webdriver
import allure
from selenium.webdriver.edge.service import Service as EdgeService
edge_path = EdgeService(r'C:\Users\Roscoe\Desktop\учеба тест\учеба тест\Pyton\msedgedriver.exe')

from form.Main import Main

@allure.title('Корректность отображения цветов заполненных и незаполненного полей')
@allure.description('Тест проверяет, что форма корректно реагирует на заполненные '
                   'и на не заполненные поля. ')
@allure.feature('ERROR')
@allure.severity('NORMAL')
def test_form_fields_color():
    browser = webdriver.Edge(service=edge_path)

    with allure.step('Открыть страницу формы в браузере Edge'):
        main_page = Main(browser)

    with allure.step('Заполнить форму данными. Поле zip_code оставить пустым'):
        main_page.filling_out_form('Иван', 'Петров', 'Ленина, 55-3', 'test@skypro.com',
                                   '+7985899998787', '', 'Москва', 'Россия', 'QA', 'SkyPro')

    with allure.step('Кликнуть на кнопку Submit'):
        main_page.submit_form()

    zip_code_field = 'rgba(248, 215, 218, 1)'
    with allure.step(f'Проверить, что незаполненное поле zip-code подсвечивается {zip_code_field}'):
        color_zip = main_page.zip_code_error()
        assert color_zip == zip_code_field

    color_field = 'rgba(209, 231, 221, 1)'
    with allure.step(f'Проверить, что заполненные поля (кроме zip-code) подсвечиваются {color_field}'):
        color_other_fields = main_page.fields_success()
        assert color_other_fields == color_field

    with allure.step('Закрыть браузер'):
        browser.quit()
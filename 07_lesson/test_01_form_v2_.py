from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
edge_path = EdgeService(r'C:\Users\Roscoe\Desktop\учеба тест\учеба тест\Pyton\msedgedriver.exe')

from form.Main import Main


def test_form_fields_color():
    browser = webdriver.Edge(service=edge_path)

    main_page = Main(browser)
    main_page.filling_out_form('Иван', 'Петров', 'Ленина, 55-3', 'test@skypro.com',
                                   '+7985899998787', '', 'Москва', 'Россия', 'QA', 'SkyPro')

    main_page.submit_form()

    color_zip = main_page.zip_code_error()
    zip_code_field = 'rgba(248, 215, 218, 1)'
    assert color_zip == zip_code_field

    color_other_fields = main_page.fields_success()
    color_field = 'rgba(209, 231, 221, 1)'
    assert color_other_fields == color_field

    browser.quit()

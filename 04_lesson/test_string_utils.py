import pytest
from string_processor import StringUtils

stringUtils = StringUtils()


@pytest.mark.pozitiv_test
@pytest.mark.parametrize('string, result', [('текст', 'Текст'),  # кириллица
                                            ('text', 'Text'),    # латиница
                                            ('Text', 'Text'),  # заглавная буква
                                            ('well done', 'Well done')])  # несколько слов
def test_capitalize(string, result):
    stringUtils = StringUtils()
    assert stringUtils.capitalize(string) == result


@pytest.mark.negativ_test
@pytest.mark.parametrize('string, result', [('  ', '  '),  # пробел
                                            ('123', '123'),  # цифры
                                            ('', ''),   # пустое поле
                                            ('!*!', '!*!')])  # символы
def test_capitalize_negative(string, result):
    stringUtils = StringUtils()
    assert stringUtils.capitalize(string) == result


@pytest.mark.pozitiv_test
@pytest.mark.parametrize('string, result', [(' Text', 'Text'),  # латиница
                                            (' текст', 'текст'),  # кириллица
                                            ('Text', 'Text')])  # без пробела в начале
def test_trim(string, result):
    stringUtils = StringUtils()
    assert stringUtils.trim(string) == result


@pytest.mark.negativ_test
@pytest.mark.parametrize('string, result', [(' 123', '123'),  # цифры
                                            (' ', ''),  # пробел
                                            ('', ''),  # пустое поле
                                            (' !*!', '!*!')])  # символы
def test_trim_negative(string, result):
    stringUtils = StringUtils()
    assert stringUtils.trim(string) == result


@pytest.mark.pozitiv_test
@pytest.mark.parametrize('string, simbol, result', [('Text', 'x', True),  # строчная латиница совпадает
                                                    ('Text', 'T', True),  # заглавная латиница совпадает
                                                    ('Текст', 'к', True),  # строчная кириллица совпадает
                                                    ('ТекCт', 'C', True),  # заглавная кириллица совпадает
                                                    ('Text', 'l', False),  # латиница не совпадает
                                                    ('Текст', 'й', False),  # кириллица не совпадает
                                                    ('123', '2', True),  # число совпадает
                                                    ('123', '5', False)])  # число не совпадает
def test_contains_pozitive(string, simbol, result):
    stringUtils = StringUtils()
    assert stringUtils.contains(string, simbol) == result


@pytest.mark.negativ_test
@pytest.mark.parametrize('string, simbol, result', [('Text', 'Т', False),  # слово на латинице, символ на кириллице
                                                    ('Текст', 'T', False),  # слово на кириллице, символ на латинице
                                                    ('еж', 'ё', False),  # йотонированная гласная
                                                    ('', '', False)])  # пустое поле !!!
def test_contains_negative(string, simbol, result):
    stringUtils = StringUtils()
    assert stringUtils.contains(string, simbol) == result


@pytest.mark.pozitiv_test
@pytest.mark.parametrize('string, simbol, result', [('Wellcome', 'come', 'Well'),  # несколько символов
                                                    ('Wellcome', 'o', 'Wellcme'),  # один символ
                                                    ('Well bell', 'ell', 'W b'),  # одинаковые символы в разных словах
                                                    ('Wellcome', 'Wellcome', ''),  # полное удаление
                                                    ('Well well', 'Well', ' well')])  # одинаковые слова с заглавной и строчной буквы
def test_delete_symbol_pozitive(string, simbol, result):
    stringUtils = StringUtils()
    assert stringUtils.delete_symbol(string, simbol) == result


@pytest.mark.negativ_test
@pytest.mark.parametrize('string, simbol, result', [('', '', ''),  # пустые поля
                                                    ('Well', '', 'Well'),  # отсутствие символа
                                                    ('', 'a', ''),  # отсутствие строки
                                                    ('Well', 'q', 'Well')])  # нет исходного символа
def test_delete_symbol_negative(string, simbol, result):
    stringUtils = StringUtils()
    assert stringUtils.delete_symbol(string, simbol) == result

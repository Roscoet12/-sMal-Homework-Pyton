### -sMal-Homework-Pyton
## Проект по автоматизации тестирования

### Проект для автоматизации тестирования с помощью Python.

### Необходимые библиотеки:
```
pytest
selenium
requests
python-dotenv
sqlalchemy
psycopg2-binary
allure-pytest
```

###  Установка и настройка:
1. Установите репозиторий:
git clone  [GitHub](https://github.com/Roscoet12/-sMal-Homework-Pyton.git)
2. Откройте проект в PyCharm
3. Установите необходимые библиотеки:
```
pip install -r requirements.txt 
```

###  Для запуска тестов используйте команду:
```
pytest
```

###  Для генерации результатов тестов с помощью allure используйте команду:
```
python -m pytest --alluredir allure-result
```

###  Для конвертации результатов тестов в отчет с помощью allure используйте команду:
```
allure serve allure-result
```
# Веб-приложение для определения заполненных форм
Это веб-приложение определяет тип заполненной формы на основе шаблонов, хранящихся в базе данных. Приложение принимает POST-запросы с данными формы и возвращает имя соответствующего шаблона или описание полей с их типами, если шаблон не найден.

## Установка и запуск 
1. *Клонирование репозитория:*
    ```git cline https://github.com/TimurBelyanin/form_template_matching.git```
2. *Переход в директорию:*
    ```cd form_template_matching```
3. *Создание виртуального окружения:*
    ```python3 -m venv venv```
4. *Активация виртуального окружения:*
    ```source venv/bin/activate```
5. *Установка зависимостей:*
    ```pip install -r requirements.txt```
6. *Запуск приложения:*
    ```pyhon app.py```

## Тестирование 
Для тестирования приложения используйте скрипт `test_requests.py`. Он содержит примеры POST-запросов с разными данными, которые проверяют различные сценарии работы приложения. Запустите скрипт командой:
```python test_requests.py```
Результаты тестов будут выведены в консоль.

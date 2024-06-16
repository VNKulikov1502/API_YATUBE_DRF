# YATUBE_API

## Описание

Проект спроектирован на Django REST Framework. Содержит в себе только API для yatube.

## О проекте

API разработан в рамках обучения на Яндекс Практикум по курсу python-разработчик.
Проект является учебным 

### Шаги установки

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/VNKulikov1502/api_final_yatube.git
    ```
   Перейдите в директорию проекта

2. Создайте виртуальное окружение и активируйте его:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Выполните миграции базы данных:
    ```bash
    python manage.py migrate
    ```

5. Создайте суперпользователя:
    ```bash
    python manage.py createsuperuser
    ```

6. Запустите сервер разработки:
    ```bash
    python manage.py runserver
    ```
## Примеры запросов и ответов:
### GET: api/v1/posts/
```json
{
"count": 123,
"next": "http://api.example.org/accounts/?offset=400&limit=100",
"previous": "http://api.example.org/accounts/?offset=200&limit=100",
"results": [
{}
]
}
```
### GET: api/v1/posts/{post_id}/comments/{id}/
```json
{
"id": 0,
"author": "string",
"text": "string",
"created": "2019-08-24T14:15:22Z",
"post": 0
}
```
### Полную документацию API можно получить по эндпоинту http://127.0.0.1:8000/redoc/


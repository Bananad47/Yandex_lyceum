# Инструкция по запуску проекта в dev-режиме
[![Python](https://img.shields.io/badge/python-v3.9-success)](https://www.python.org/) [![Django](https://img.shields.io/badge/django-v3.2-success)](https://www.djangoproject.com/)
[![Python package](https://github.com/Bananad47/Yandex_lyceum/actions/workflows/python-package.yml/badge.svg)](https://github.com/Bananad47/Yandex_lyceum/actions/workflows/python-package.yml)
## Создание виртуального окружения
```
python -m venv venv
```
### Запуск виртуального окружения
Для Windows
```
.\venv\Scripts\Activate
```
Для macOS/Linux
```
source venv/bin/Activate
```
### Выход из виртуального окружения
```
deactivate
```

## Запуск проекта
```
git clone https://github.com/Bananad47/Yandex_lyceum
pip install -r requirements\main.txt
cd lyceum
cd lyceum
```
#### Нужно переименовать файл `.env_sample` в `.env`. Вместо `YOUR_SECRET_KEY ` указать свой секретный ключ. Вместо `DEBUG_STATE` указать True или False, в зависимости от того хотите вы или нет включить debug. А `HOST_LIST` заменить на список разрешенных ip адресов, например `['198.211.99.20', 'localhost', '127.0.0.1']` или `["*"]`, если хотите разрешить все ip адресы.


#### После чего мы можем запускать проект.

```
cd ..
python manage.py runserver
```

## Зависимости
#### В проекте есть 3 файла с зависимостями: `dev_req.txt`, `test_req.txt` и `main_req.txt`.
#### `main_req.txt` - список зависимостей для запуска проекта.
#### `dev_req.txt` - список зависимостей для разработки.
#### `test_req.txt` - список зависимостей для тестирования.

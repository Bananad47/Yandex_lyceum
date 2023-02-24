# Инструкция по запуску проекта в dev-режиме
[![Python](https://img.shields.io/badge/python-v3.9-success)](https://www.python.org/) [![Django](https://img.shields.io/badge/django-v3.2-success)](https://www.djangoproject.com/)
[![Python package](https://github.com/Bananad47/Yandex_lyceum/actions/workflows/python-package.yml/badge.svg)](https://github.com/Bananad47/Yandex_lyceum/actions/workflows/python-package.yml)
[![Django CI](https://github.com/Bananad47/Yandex_lyceum/actions/workflows/django.yml/badge.svg)](https://github.com/Bananad47/Yandex_lyceum/actions/workflows/django.yml)
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
pip install -r requirements\prod_req.txt
cd lyceum
```

#### Нужно переименовать файл `.env_sample` в `.env`. 
#### Вместо `YOUR_SECRET_KEY ` указать свой секретный ключ. 
#### Вместо `DEBUG_STATE` указать True или False, в зависимости от того хотите вы или нет включить debug.
#### Для включения переворачивания русских слов нужно изменить значение переменной `REVERSE_RUSSIAN_WORDS` на True, на False для выключения. 
#### А `HOST_LIST` заменить на список разрешенных ip адресов, например `['198.211.99.20', 'localhost', '127.0.0.1']` или `["*"]`, если хотите разрешить все ip адресы.


#### После чего мы можем запускать проект.

```
python manage.py runserver
```

## Зависимости
#### В проекте есть 3 файла с зависимостями: `dev_req.txt`, `test_req.txt` и `prod_req.txt`.
#### `prod_req.txt` - список зависимостей для запуска проекта.
#### `dev_req.txt` - список зависимостей для разработки.
#### `test_req.txt` - список зависимостей для тестирования.

## ER-диаграмма
[![ER diagramm](https://github.com/Bananad47/Yandex_lyceum/blob/main/ne_full.jpg)]

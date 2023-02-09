# Инструкция по запуску проекта в dev-режиме
[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/) [![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
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
#### Нужно переименовать файл `.env_sample` в `.env`, а вместо `YOUR_SECRET_KEY ` указать свой секретный ключ. После чего мы можем запускать проект.

```
cd ..
python manage.py runserver
```

## Зависимости
#### В проекте есть 3 файла с зависимостями: `dev_req.txt`, `test_req.txt` и `main_req.txt`.
#### `main_req.txt` - список зависимостей для запуска проекта.
#### `dev_req.txt` - список зависимостей для разработки.
#### `test_req.txt` - список зависимостей для тестирования.




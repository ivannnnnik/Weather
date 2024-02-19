# Weather

## Инструкция по запуску

1. Поднять контейнер с Flask приложением

```commandline
sudo docker-compose up -d --build
```

**! В окружении предоставляю свой токен для сервиса - https://home.openweathermap.org/ , имеются ограниения по кол-ву
запросов, в случае необходимости заменить на свой в .env**

## Тестовые данные

**В базе будут находиться 5 тестовых пользователей с id 1-5**

## Endpoints

1. http://127.0.0.1:5000/update_user_balance - обновление баланса пользователя

## Пример запроса

POST http://127.0.0.1:5000/update_user_balance \
body = {"userId":1, "city": "Moscow"}

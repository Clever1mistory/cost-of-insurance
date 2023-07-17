
# Readme файл для REST API сервиса расчета стоимости страхования

## Описание

Этот REST API сервис предназначен для расчета стоимости страхования в зависимости от типа груза и объявленной стоимости. Тарифы загружаются из файла JSON или могут быть переданы в виде JSON структуры.

##API документация

API документация доступна по адресу [http://localhost:9999](http://localhost:9999). Здесь вы можете ознакомиться со всеми доступными эндпоинтами.

## Установка и запуск

1. Установите Docker на вашу машину, если он еще не установлен.
2. Склонируйте репозиторий и перейдите в его директорию.

```
git clone <repository_url>
cd <repository>
```

3. Загрузите необходимые зависимости с помощью команды:

```
pip install requirements.txt
```

4. Запустите сервис с помощью Docker:

```
docker-compose up
```

## Использование

### Загрузка тарифов

Тарифы для расчета страховой стоимости загружаются из файла JSON или указываются в формате JSON структуры. Пример структуры JSON для тарифов:

```
[
  {
    "cargo_type": "Glass",
    "rate": 0.15,
    "date": "2022-10-01"
  },
  {
    "cargo_type": "Wood",
    "rate": 0.1,
    "date": "2022-10-01"
  }
]
```

### Расчет стоимости страхования

Для расчета стоимости страхования, отправьте POST запрос на URL `http://localhost:9999/api/calculation` с параметрами:

- `cargo_type` - тип груза (Glass, Wood и т.д.)
- `declared_value` - объявленная стоимость

### Ответ

Сервис вернет JSON объект с полем `insurance_cost`, содержащим расчитанную стоимость страхования в зависимости от указанного типа груза и даты.

Пример ответа:

```
{
  "insurance_cost": 15
}
```

## TODO

Список задач, которые можно выполнить для улучшения сервиса:

- Добавить API эндпоинты для управления тарифами (обновление, удаление).
- Добавить логирование запросов и ошибок.
- Обеспечить безопасность API (авторизация, аутентификация).
- Обеспечить поддержку различных форматов для загрузки тарифов (XML, CSV и т.д.).
- Оптимизировать и улучшить производительность кода.

## Авторы

- Clever1mistory
- clever1mistory@gmail.com

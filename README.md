# API обмена валют #

## Документация ##
Подробное техническое задание и требования к функционалу описаны в [docs/specification.md](docs/specification.md).

## Структура проекта ##

```
project/
│
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── endpoints/
│   │   │   ├── __init__.py
│   │   │   ├── v1/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── currency.py
│   │   │   │   └── users.py
│   │   │   ├── v2/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── currency.py
│   │   │   │   └── users.py
│   │   │   ├── currency.py
│   │   │   ├── users.py
│   │   │   └── ...
│   │   ├── repository/
│   │   │   ├── __init__.py
│   │   │   └── user.py
│   │   ├── schemas/
│   │   │   ├── __init__.py
│   │   │   ├── currency.py
│   │   │   └── user.py
│   │   └── services/
│   │   │   ├── __init__.py
│   │   │   └── users.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   ├── fake_db.py
│   │   └── security.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── external_api.py
│   └── __init__.py
├── tests/
│   ├── __init__.py
│   ├── test_endpoints.py
│   └── test_models.py
├── .env
├── .gitignore
├── main.py
├── pyproject.toml
├── README.md
└── requirements.txt
```

### Краткий обзор структуры: ###

    - В папке endpoints лежат файлы с конечными точками (как минимум две группы конечных точек);
    - В папке models лежат модели Pydantic;
    - В ядре (core) лежат файлы, касающиеся настроек приложения и безопасности;
    - В папке utils размещена логика работы с внешним API.

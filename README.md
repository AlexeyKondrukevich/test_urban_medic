# test_urban_medic
Онлайн клиника

![https://github.com/AlexeyKondrukevich](https://img.shields.io/badge/Developed%20by-Kondr-blue)
## Запуск проекта

- Клонировать репозиторий
- Создать файл .env со следующим содержанием:

```
SECRET_KEY=django-insecure-qh_z59y8t)kjoun$tr*)nnrwx@6o4kf!+oi7y77$+53=@bsslx
DEBUG=True
ALLOWED_HOSTS=localhost 127.0.0.1 0.0.0.0

POSTGRES_USER=clinic
POSTGRES_PASSWORD= clinic

DB_HOST=db
DB_PORT=5432
DB_ENGINE=django.db.backends.postgresql_psycopg2
DB_NAME= clinic
```

- В директории test_urban_medic выполнить

```
sudo docker-compose up -d
```

Документацию к API с примерами запросов можно посмотреть [тут](http://127.0.0.1:8000/swagger/) (при развернутом проекте)
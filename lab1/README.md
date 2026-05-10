# Lab 1: Apache Airflow + Docker Compose

## Инструкция по запуску:
1. Перейдите в папку `lab1`: `cd lab1`
2. Запустите docker-compose: `docker-compose up -d --build`
3. Дождитесь пока контейнеры `postgres`, `airflow-init`, `airflow-webserver` и `airflow-scheduler` перейдут в состояние `healthy` (можно проверить через `docker ps`).
4. Откройте в браузере `http://localhost:8080`.
5. Логин и пароль: `admin` / `admin`.
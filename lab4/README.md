# Lab 4: Loki + Prometheus + Grafana

## Инструкция по запуску:
1. Эта лаба использует файлы из `lab2` (образы и скрипты Spark/Airflow). Убедитесь, что `lab2` настроена.
2. Перейдите в папку `lab4`: `cd lab4`
3. Запустите docker-compose: `docker-compose up -d`
4. Дождитесь запуска всех контейнеров.
5. Сервисы доступны по адресам:
   - Grafana: `http://localhost:3000`
   - Prometheus: `http://localhost:9090`
   - Airflow: `http://localhost:8080`
   - Spark: `http://localhost:4040`

## Что проверить:
1. Запустите DAG `spark_submit_dag` в Airflow (это сгенерирует логи и метрики).
2. Зайдите в Grafana (`http://localhost:3000`).
3. Подключите Data Sources (Admin -> Data Sources):
   - **Loki**: URL `http://loki:3100` -> Save & Test
   - **Prometheus**: URL `http://prometheus:9090` -> Save & Test
4. Перейдите в раздел Explore.
5. Выберите источник **Loki**, укажите фильтр: `{job="airflow_logs"}` или поищите логи со строкой `spark_submit`.
6. Выберите источник **Prometheus**, попробуйте найти метрику из Airflow или метрику Spark (например, метрики мастера по пути `/metrics/master/prometheus`, которые Прометей собирает).
7. Создайте Dashboard и добавьте туда две панели: одну с метрикой из Prometheus, другую с логами из Loki. Сделайте скриншот для отчета.

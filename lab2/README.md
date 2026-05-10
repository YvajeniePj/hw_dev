# Lab 2: Apache Airflow + Spark

## Инструкция по запуску:
1. Перейдите в папку `lab2`: `cd lab2`
2. Запустите docker-compose: `docker-compose up -d --build`
3. Дождитесь пока все контейнеры (postgres, spark, airflow) будут готовы.
4. Откройте в браузере `http://localhost:8080` (Airflow) и `http://localhost:4040` (Spark).
5. Логин и пароль для Airflow: `admin` / `admin`.
6. Создайте подключение к Spark в Airflow: Admin -> Connections -> + Add a new record.
   - Connection Id: `spark_local`
   - Connection Type: `Spark`
   - Host: `spark://spark-master`
   - Port: `7077`
   - Нажмите Save.
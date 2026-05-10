FROM apache/airflow:2.7.1
WORKDIR /opt/airflow
USER root
RUN apt update && apt -y install procps default-jre
USER airflow
COPY ./dags ./dags/
COPY ./spark ./spark/
RUN pip install apache-airflow-providers-apache-spark==4.1.1 pyspark==3.5.0

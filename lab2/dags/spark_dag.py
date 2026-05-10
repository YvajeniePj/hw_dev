from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'spark_submit_dag',
    default_args=default_args,
    description='A simple DAG to submit Spark job',
    schedule_interval=timedelta(days=1),
    catchup=False,
) as dag:

    spark_job = SparkSubmitOperator(
        task_id='my_spark_job',
        application='/opt/airflow/spark/my_script.py',
        name='my_spark_job',
        conn_id='spark_local',
        dag=dag
    )

    spark_job

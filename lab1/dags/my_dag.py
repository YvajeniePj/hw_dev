from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def count_numbers():
    total = sum(range(1, 1000))
    print(f"Sum of numbers from 1 to 1000 is {total}")
    return total

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'calculate_sum_dag',
    default_args=default_args,
    description='A simple DAG to calculate sum',
    schedule_interval=timedelta(days=1),
    catchup=False,
) as dag:

    task1 = PythonOperator(
        task_id='print_hello',
        python_callable=lambda: print("Hello from Airflow!")
    )

    task2 = PythonOperator(
        task_id='calculate_sum',
        python_callable=count_numbers
    )

    task1 >> task2

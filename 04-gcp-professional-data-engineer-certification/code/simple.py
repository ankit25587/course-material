from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime


dag = DAG('hello_world_dag', description='Hello world example', schedule_interval='*/1 * * * *', start_date=datetime(2021, 1, 1), catchup=False)


def print_hello():
    return ("Hello world!")


dummy_task_1 = DummyOperator(
 task_id = 'dummy_task',
 retries = 0,
 dag = dag)
 
hello_task_2 = PythonOperator(
    task_id = 'hello_task', 
    python_callable = print_hello, 
    dag = dag)


dummy_task_1 >> hello_task_2
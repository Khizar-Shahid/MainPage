from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'scrapy_dag',
    default_args=default_args,
    description='Run Scrapy Spider',
    schedule_interval=timedelta(days=1),
)

run_scrapy_spider = BashOperator(
    task_id='run_scrapy_spider',
    bash_command='scrapy runspider /dags/my_scraper/my_scraper/spiders/MySpider.py',
    dag=dag,
)

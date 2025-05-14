from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'start_date': datetime(2023, 1, 1),
}

with DAG(
    'amazon_pipeline',
    default_args=default_args,
    schedule='@daily',
    catchup=False,
) as dag:

    run_script = BashOperator(
        task_id='populate_internal_stage',
        bash_command='python #/D:/amazon_snowpark/populate_internal_stage.py',
    )
    
    run_script

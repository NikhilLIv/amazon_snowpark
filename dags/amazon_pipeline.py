from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from pathlib import Path
import sys
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

# Add script directory to path
script_path = Path("D:/amazon_snowpark")
sys.path.append(str(script_path))

from populate_internal_stage import main

default_args = {
    'start_date': datetime(2023, 1, 1),
}

with DAG(
    'amazon_pipeline',
    default_args=default_args,
    schedule='@daily',
    catchup=False,
) as dag:

    first_step = PythonOperator(
        task_id='populate_internal_stage',
        python_callable=main,
    )
    
    first_step

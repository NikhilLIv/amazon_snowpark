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
script_path = Path("D:/amazon_snowpark") #my local path for python scripts
sys.path.append(str(script_path))

from populate_internal_stage import populate_internal_stage
from populate_source_tables_from_stage import populate_source_tables
from source_to_curated_fr import source_to_curated_fr
from source_to_curated_in import source_to_curated_in
from source_to_curated_us import source_to_curated_us

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
        python_callable=populate_internal_stage,
    )
    
    second_step = PythonOperator(
        task_id='populate_source_tables',
        python_callable=populate_source_tables,
    )
    
    third1_step = PythonOperator(
        task_id='source_to_curated_fr',
        python_callable=source_to_curated_fr,
    )
    
    third2_step = PythonOperator(
        task_id='source_to_curated_in',
        python_callable=source_to_curated_in,
    )
    
    third3_step = PythonOperator(
        task_id='source_to_curated_us',
        python_callable=source_to_curated_us,
    )
    
    first_step >> second_step
    second_step >> third1_step
    second_step >> third2_step
    second_step >> third3_step

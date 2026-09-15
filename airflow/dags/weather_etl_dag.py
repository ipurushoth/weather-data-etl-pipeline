from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="weather_etl_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["weather", "etl"],
) as dag:

    extract = BashOperator(
        task_id="extract_weather",
        bash_command="cd /opt/airflow/project && python src/extract.py"
    )

    transform = BashOperator(
        task_id="transform_weather",
        bash_command="cd /opt/airflow/project && python src/transform.py"
    )

    load = BashOperator(
        task_id="load_weather",
        bash_command="cd /opt/airflow/project && python src/load.py"
    )

    extract >> transform >> load
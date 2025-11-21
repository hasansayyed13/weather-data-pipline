from airflow.operators.python import PythonOperator
from scripts.extract import fetch_data
from scripts.transfor import tranform_data
from scripts.load import connect_to_db


#comming soon



from transfor import tranform_data
import logging
import pandas as pd
from sqlalchemy import create_engine

def connect_to_db(data):
    try:
        logging.info("Connecting to DB")
        engine = create_engine("mysql+pymysql://root:1234@localhost:3306/Weather_Data")
        logging.info('Successfully connected to database')

        try:
            logging.info("Saving Data  to DB (Mysql)")
            df = pd.DataFrame(data)
            df.to_sql(
                "weather_data",
                con=engine,
                if_exists='append',
                index=False
            )
        except Exception as e:
            logging.error(f"Failed to Save Data into DB (MYSQL){e}")

    except Exception as e:
        logging.error(f"Connection Failed !! : {e}")





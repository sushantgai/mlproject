import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql


load_dotenv()
host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")

def read_sql_data():
    logging.info("Reading Mysql Database")
    try:
        mydb = pymysql.connect(host=host,user=user,password=password,database=db)
        logging.info("Connected to Mysql Database")
        df = pd.read_sql("SELECT * FROM student", con=mydb)
        print(df.head())
        return df
    except Exception as ex:
        raise CustomException(ex,sys) 
import os
import pymysql
import sys
from src.mlproject2.logger import logging
from src.mlproject2.exception import CustomException
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")




def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb=pymysql.connect(host=host,user=user,password=password,database=db)

        logging.info("Connection Established",mydb) 
        df=pd.read_sql("select * from student",mydb)
        print(df.head())
        return df

    except Exception as e:
        raise CustomException(e, sys)    
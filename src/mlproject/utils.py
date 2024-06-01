# utils.py file me is file me hum sare vo function banate hai jo 'Generic' hote hai yani ye function common hote hai aur hum bas ek bar bana dete aur jis bhi file me jarurat padti hai toh import kar lete hai
import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql
import pickle
import numpy as np

load_dotenv()

host=os.getenv("host")
user=os.getenv("user")
password=os.getenv("password")
db=os.getenv("db")
# Generic Fundtion ----> 
def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        mydb=pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info("Connection Established",mydb)
        df=pd.read_sql_query('Select * from students',mydb)
        print(df.head())

        return df



    except Exception as ex:
        raise CustomException(ex)
    
    
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
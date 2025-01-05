import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
import pandas as pd
from dataclasses import dataclass
from src.mlproject.utils import read_sql_data
from sklearn.model_selection import train_test_split

@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join("artificats","train.csv")
    test_data_path:str = os.path.join("artificats","test.csv")
    raw_data_path:str = os.path.join("artificats","raw.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
    
    def initate_data_ingestion(self):
        try:
            df = read_sql_data()
            logging.info("Data Ingestion is successful")

            # Ensure the directory for saving data exists; create it if it doesn't
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)


            # Save the entire dataset to a CSV file as raw data
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("Data saved in raw.csv")


            # Split the dataset into training and testing sets with an 80-20 split
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            # Save the training and testing sets to CSV files
            train_set.to_csv(self.ingestion_config.train_data_path,index=False)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False)
            logging.info("Data saved in train.csv and test.csv")



            return (self.ingestion_config.train_data_path,self.ingestion_config.test_data_path)

        except Exception as e:
            raise CustomException(e,sys)

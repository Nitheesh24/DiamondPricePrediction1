import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation

data_ingestion_instance = DataIngestion()

try:
    # Call the instance method on the created instance
    train_data_path, test_data_path = data_ingestion_instance.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_arr,test_arr,obj_path = data_transformation.initiate_data_transformation(train_data_path,test_data_path)
except CustomException as e:
    print(f"Error: {e}")
    # Handle the exception gracefully, maybe log it or provide a default value
    train_data_path, test_data_path = None, None




    





# Continue with the rest of your code using train_data_path and test_data_path

       
    
    
    
    
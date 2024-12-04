from train import train_model
from test import test_model
import pandas as pd
from prepricessing import preprocess_train_data
from prepricessing import preprocess_testing_data


train_model(file_name="train.csv",model_name='XGBRegressor')
test_model(file_name='test.csv',model_name='XGBRegressor') 
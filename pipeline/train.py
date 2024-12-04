import pandas as pd
import pickle 
from prepricessing import preprocess_train_data
import columns
import xgboost as xgb
import hiperparameters

def train_model(file_name: str = 'train.csv', model_name: str = 'XGBRegressor'):
    # loading data
    ds = pd.read_csv('D:/3Kurs/1Sem/SS/rgr/data/' + file_name)
    
    ds = preprocess_train_data(ds)
    
    X = ds[columns.X_column]
    y = ds[columns.y_column]
    
    XGBRegressor = xgb.XGBRegressor(**hiperparameters.param_grid)
    XGBRegressor.fit(X, y)
    
    with open(f'D:/3Kurs/1Sem/SS/rgr/models/XGBRegressor.pickle', 'wb') as handle:
        pickle.dump(XGBRegressor, handle, protocol=pickle.HIGHEST_PROTOCOL)
   

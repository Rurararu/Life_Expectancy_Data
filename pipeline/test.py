import pandas as pd
import pickle
from prepricessing import preprocess_testing_data
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

import columns


def test_model(file_name: str = 'test.csv', model_name: str = 'XGBRegressor'):
    
       # loading data
    ds = pd.read_csv('D:/3Kurs/1Sem/SS/rgr/data/' + file_name)
    
    ds = preprocess_testing_data(ds)
    
    X = ds[columns.X_column]
    y = ds[columns.y_column]
    
    with open(f'D:/3Kurs/1Sem/SS/rgr/models/{model_name}.pickle', 'rb') as f:
        model = pickle.load(f)
        
    predictions = model.predict(X)
    pd.DataFrame(predictions).to_csv('D:/3Kurs/1Sem/SS/rgr/data/predictions.csv', index=False)
    
    mae = mean_absolute_error(y, predictions)
    mse = mean_squared_error(y, predictions)
    rmse = mean_squared_error(y, predictions, squared=False)  # або np.sqrt(mse)
    r2 = r2_score(y, predictions)

    # Виводимо результати
    print("Mean Absolute Error (MAE):", mae)
    print("Mean Squared Error (MSE):", mse)
    print("Root Mean Squared Error (RMSE):", rmse)
    print("R-squared (R2):", r2)

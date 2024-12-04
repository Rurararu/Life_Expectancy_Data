import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
from statsmodels.imputation import mice
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder
import pickle
# for Q-Q plots
import scipy.stats as stats
import columns 
import warnings
warnings.simplefilter('ignore')

def preprocess_train_data(ds: pd.DataFrame) -> pd.DataFrame:
    
    def impute_na(df, variable, value):
        return df[variable].fillna(value)
    
    # remove all rows with more than 5 missing values
    missing_rows = ds[ds.isnull().sum(axis=1) >= 5]
    ds = ds.drop(missing_rows.index)

    # And now those 10 lines, of which only data for 2013 in 10 countries are known
    ds = ds[~ds['Country'].isin(columns.countries_to_remove)]
    
    percentile_impute_columns = dict()
    for column in columns.percentile_impute_columns:
        percentile_impute_columns[column] = ds[column].quantile(0.01)
        ds[column] = impute_na(ds, column, percentile_impute_columns[column])
        
    median_impute_columns = dict()
    for column in columns.median_impute_columns:
        median_impute_columns[column] = ds[column].median()
        ds[column] = impute_na(ds, column, median_impute_columns[column])
    
    def find_skewed_boundaries(df, variable, distance):

        IQR = df[variable].quantile(0.75) - df[variable].quantile(0.25)

        lower_boundary = df[variable].quantile(0.25) - (IQR * distance)
        upper_boundary = df[variable].quantile(0.75) + (IQR * distance)

        return upper_boundary, lower_boundary
    
    outliers_left_columns = dict()
    for column in columns.outliers_left_columns:
        upper_boundary, lower_boundary = find_skewed_boundaries(ds, column, 2)
        median_value = ds[column].median()
        ds.loc[ds[column] < lower_boundary, column] = median_value
        outliers_left_columns[column] = median_value

    outliers_right_columns = dict()
    for column in columns.outliers_right_columns:
        upper_boundary, lower_boundary = find_skewed_boundaries(ds, column, 2)
        median_value = ds[column].median()
        ds.loc[ds[column] > upper_boundary, column] = median_value
        outliers_right_columns[column] = median_value
    
    def creat_Region_col(df, mapping=columns.country_to_region):
        df["Region"] =df['Country'].map(columns.country_to_region) 

    creat_Region_col(ds)
    
    ds = ds.drop(['Country', 'Infant_deaths'], axis=1)
    
    columns_encoding = dict()
    for column in columns.columns_encoding:
        tmp = pd.get_dummies(ds[column], prefix=column)
        tmp = tmp.astype(int)
        columns_encoding = tmp
        ds = ds.drop(column, axis=1)
        ds = pd.concat([ds, columns_encoding], axis=1)
    
    ds = ds.drop('Status_Developing', axis=1)
    
    scaler = MinMaxScaler()
    ds[columns.colmns_to_scale] = scaler.fit_transform(ds[columns.colmns_to_scale])
    
    param_dict ={'percentile_impute_columns':percentile_impute_columns,
                  'median_impute_columns':median_impute_columns,
                  'outliers_left_columns':outliers_left_columns,
                  'outliers_right_columns':outliers_right_columns,
                  'columns_encoding':columns_encoding
    }
    
    with open('D:/3Kurs/1Sem/SS/rgr/pipeline/param_dict.pickle', 'wb') as handle:
        pickle.dump(param_dict, handle, protocol=pickle.HIGHEST_PROTOCOL)
        
    ds.to_csv('D:/3Kurs/1Sem/SS/rgr/data/train_look.csv', index=False)
    
    return ds


def preprocess_testing_data(ds: pd.DataFrame) -> pd.DataFrame:
    
    with open('D:/3Kurs/1Sem/SS/rgr/pipeline/param_dict.pickle', 'rb') as handle:
        param_dict = pickle.load(handle)
    
    def impute_na(df, variable, value):
        return df[variable].fillna(value)
    
    # remove all rows with more than 5 missing values
    missing_rows = ds[ds.isnull().sum(axis=1) >= 5]
    ds = ds.drop(missing_rows.index)

    # And now those 10 lines, of which only data for 2013 in 10 countries are known
    ds = ds[~ds['Country'].isin(columns.countries_to_remove)]
    
    for column in columns.percentile_impute_columns:
        percentile_impute_columns = param_dict['percentile_impute_columns'][column]
        ds[column] = impute_na(ds, column, percentile_impute_columns)
        
    for column in columns.median_impute_columns:
        median_impute_columns = param_dict['median_impute_columns'][column]
        ds[column] = impute_na(ds, column, median_impute_columns)

    def find_skewed_boundaries(df, variable, distance):

        IQR = df[variable].quantile(0.75) - df[variable].quantile(0.25)

        lower_boundary = df[variable].quantile(0.25) - (IQR * distance)
        upper_boundary = df[variable].quantile(0.75) + (IQR * distance)

        return upper_boundary, lower_boundary

    for column in columns.outliers_left_columns:
        upper_boundary, lower_boundary = find_skewed_boundaries(ds, column, 2)
        median_value = param_dict['outliers_left_columns'][column]
        ds.loc[ds[column] < lower_boundary, column] = median_value
        
    for column in columns.outliers_right_columns:
        upper_boundary, lower_boundary = find_skewed_boundaries(ds, column, 2)
        median_value = param_dict['outliers_right_columns'][column]
        ds.loc[ds[column] > upper_boundary, column] = median_value
        
    def creat_Region_col(df, mapping=columns.country_to_region):
        df["Region"] =df['Country'].map(columns.country_to_region) 

    creat_Region_col(ds)
    
    ds = ds.drop(['Country', 'Infant_deaths'], axis=1)
    
    for column in columns.columns_encoding:
        tmp = pd.get_dummies(ds[column], prefix=column)
        tmp = tmp.astype(int)
        columns_encoding = tmp
        ds = ds.drop(column, axis=1)
        ds = pd.concat([ds, columns_encoding], axis=1)
    
    ds = ds.drop('Status_Developing', axis=1)
    
    scaler = MinMaxScaler()
    ds[columns.colmns_to_scale] = scaler.fit_transform(ds[columns.colmns_to_scale])

    return ds

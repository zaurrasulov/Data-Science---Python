import os
import pandas as pd
import numpy as np
from sklearn.impute import KNNImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import KNNImputer

#read excel file
df = pd.read_excel(r'C:\Users\Zaur\Desktop\Data science\Missing values\missing_values.xlsx')

#defining cat variables and getting dummies

# get_dummies is a function converting categorical data to dummy variables
cat_variables = df[['Gender']]
cat_dummies = pd.get_dummies(cat_variables, drop_first=True)
print(cat_dummies)

#deleting 'Gender' column
df = df.drop(['Gender'], axis=1)

#joining the dataframe and dummy variables
df = pd.concat([df, cat_dummies], axis=1)
print(df.head())

#defining the variables in the specific range
scaler = MinMaxScaler()
df = pd.DataFrame(scaler.fit_transform(df), columns = df.columns)
print(df.head())

#imput by kNN
imputer = KNNImputer(n_neighbors=5)
df = pd.DataFrame(imputer.fit_transform(df),columns = df.columns)
z=df.isna().any()
print(z)


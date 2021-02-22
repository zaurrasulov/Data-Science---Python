import os
import pandas as pd
import numpy as np


df = pd.read_excel(r'C:\Users\Zaur\Desktop\missing_values.xlsx')
#print(df)
print("-------------------------------------------------------")
miss = df.isnull().sum().to_frame('Missing Value Counts')
print(miss)
print("-------------------------------------------------------")


# imputing mean
missing_col = ['GPA']
for i in missing_col:
     df.loc[df.loc[:,i].isnull(),i]=df.loc[:,i].mean()
miss1=df.isnull().sum()
print(miss1)

# imputing median
missing_col = ['IELTS']
for i in missing_col:
     df.loc[df.loc[:,i].isnull(),i]=df.loc[:,i].median()
miss2=df.isnull().sum()
print(miss2)
print(df)




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


df = pd.read_csv(r'C:\Users\Zaur\Desktop\healthcare-dataset-stroke-data.csv')

# percentage of missing values
print(df.isnull().mean())

# printing all the unique values. 
print(df['work_type'].unique())

# defining the elements as the first letter
df['work_type'] = df['work_type'].astype(str).str[0]
df['Residence_type'] = df['Residence_type'].astype(str).str[0]

# splitting into train and test datasets
X_train, X_test, y_train, y_test = train_test_split(
    df[['gender', 'age', 'hypertension', 'heart_disease', 'work_type', 'Residence_type', 'stroke']],  # this time we keep the target!!
    df['stroke'],  
    test_size=0.3,  
    random_state=0)  

print(X_train.shape, X_test.shape)

# plotting the relations between the columns 
for var in ['gender', 'work_type', 'Residence_type']:
    
    fig = plt.figure()
    fig = X_train.groupby([var])['stroke'].mean().plot()
    fig.set_title('Relationship between {} and Stroke'.format(var))
    fig.set_ylabel('Mean Stroke')
    plt.show()
  
# WOE for 'work_type' column

# calculating the total amount
total_stroke = X_train['stroke'].sum()

# percentage of those with stroke
stroke = X_train.groupby(['work_type'])['stroke'].sum() / total_stroke
print(stroke)

# Those without stroke
total_non_stroke = len(X_train) - X_train['stroke'].sum()
X_train['non_stroke'] = np.where(X_train['stroke'] == 1, 0, 1)
non_stroke = X_train.groupby(
    ['work_type'])['non_stroke'].sum() / total_non_stroke
print(non_stroke)

# combining new columns into 1 dataset
new_df = pd.concat([stroke, non_stroke], axis=1)
new_df['woe'] = np.log(new_df['stroke']/new_df['non_stroke'])
print(new_df)

# general function
def woe(data, variable, target):    
    temp = data.copy() 
    total_event = data[target].sum()
    total_non_event = len(df) - data[target].sum()
    temp['non-target'] = 1 - temp[target]
    event = temp.groupby([variable])[target].sum() / total_event
    non_event = temp.groupby([variable])['non-target'].sum() / total_non_event
    prob_temp = pd.concat([event, non_event], axis=1)
    prob_temp['woe'] = np.log(prob_temp[target]/prob_temp['non-target'])
    return prob_temp['woe'].to_dict()


def integer_encode(train, test, variable, ordinal_mapping):
    train[variable] = train[variable].map(ordinal_mapping)
    test[variable] = test[variable].map(ordinal_mapping)
    
for variable in ['gender', 'work_type', 'Residence_type']:
    mappings = woe(X_train, variable, 'stroke')
    integer_encode(X_train, X_test, variable, mappings)    
    

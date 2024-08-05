import pandas as pd
import numpy as np

data= pd.read_csv('filename')

#Create Target Column (1:High Risk, 0:Low Risk)
def label_risk(row):
    if row['SMISED'] == 1:
        return 1
    if row['SMISED'] == 2:
        return 1
    if row['SMISED'] == 3:
        return 0
    else:
        return float('NaN')

data['mh_risk'] = data.apply(label_risk, axis=1)

#Drop missing values
data = data.dropna()

#Normalize datatype
data = data.astype('int64')

#Drop irrevelant variables
df = data.drop(columns=['CASEID', 'CMPSERVICE', 'IJSSERVICE', 
                        'OPISERVICE','TRAUSTREFLG', 'ANXIETYFLG', 
                        'ADHDFLG', 'CONDUCTFLG', 'DELIRDEMFLG', 
                        'BIPOLARFLG', 'DEPRESSFLG', 'ODDFLG', 
                        'PDDFLG', 'PERSONFLG', 'SCHIZOFLG', 
                        'ALCSUBFLG', 'OTHERDISFLG',
                        'RTCSERVICE', 'SPHSERVICE', 'YEAR', 'SMISED', 
                        'DIVISION', 'REGION'])

#Separate Features
X = df.drop(columns=['mh_risk'])
X.head()

#Identify Target
y = df['mh_risk'].values

##Split dataset into train and test data
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1, stratify=y)

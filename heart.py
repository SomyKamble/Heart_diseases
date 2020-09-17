# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 15:45:53 2019

@author: EGC
"""
import warnings
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd

Dataset = pd.read_csv("Stroke.csv")


print (Dataset.head())
print(Dataset.describe())

#Data Preprocessing
#Missing Data Removal

#check missing values
print ('Dataset contain null:\t',Dataset.isnull().values.any())
print ('Describe null:\n',Dataset.isnull().sum())
print ('No of  null:\t',Dataset.isnull().sum().sum())

#Replace values
Dataset['smoking_status'].fillna('Sometimes', inplace=True)
Dataset.fillna(Dataset.mean(), inplace=True)
columns = ['id','ever_married','work_type','Residence_type']
Dataset.drop(columns, inplace=True, axis=1)

x = Dataset.iloc[:, :-1].values
x1=pd.DataFrame(x)
y = Dataset.iloc[:,7].values
y1=pd.DataFrame(y)

#check missing values
print ('Dataset contain null:\t',Dataset.isnull().values.any())
print ('Describe null:\n',Dataset.isnull().sum())
print ('No of  null:\t',Dataset.isnull().sum().sum())

#Encoding categorical data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_x=LabelEncoder()
x[:,0]=labelencoder_x.fit_transform(x[:,0])

x[:,6]=labelencoder_x.fit_transform(x[:,6])
Y=pd.DataFrame(x[:,1])
onehotencoder=OneHotEncoder(categorical_features=[0])

onehotencoder=OneHotEncoder(categorical_features=[6])
x=onehotencoder.fit_transform(x).toarray()

from sklearn.decomposition import PCA
pca = PCA(n_components=2)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents
             , columns = ['principal component 1', 'principal component 2'])



   
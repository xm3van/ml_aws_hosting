#!/usr/bin/env python
# coding: utf-8

# In[1]:


#visualisation
import matplotlib.pyplot as plt 

# Data manipulation 
import pandas as pd
from sklearn.model_selection import train_test_split

# ML 
import pickle # save model essentially
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# load dataset
df_train = pd.read_csv('train.csv')

# 4Cs

## getting titles

def get_title(name):
    
    if '.' in name: 
        
        return name.split(',')[1].split('.')[0].strip()
    
    else:
        
        return "No title in name"

def shorter_titles(x):
    title = x['Title']
    
    if title in ['Capt', 'Col', 'Major']:
        return 'Officer'
    
    elif title in ['Jonkheer', 'Don', 'Dona', 'the Countess', 'Dons', 'Lady', 'Sir']:
        return 'Royalty'
    
    elif title == 'Mme':
        return 'Mrs'
    
    elif title in ['Mlle', 'Ms']:
        return 'Miss'
    
    else:
        return title
    
    

## futher corrections

df_train['Title'] = df_train['Name'].map(lambda x: get_title(x))
df_train['Title'] = df_train.apply(shorter_titles, axis=1)

df_train['Age'].fillna(df_train['Age'].median(), inplace=True)
df_train['Fare'].fillna(df_train['Fare'].median(), inplace=True)
df_train["Embarked"].fillna("S", inplace=True)

df_train.drop("Cabin", axis=1, inplace=True)
df_train.drop("Ticket", axis=1, inplace=True)
df_train.drop("Name", axis=1, inplace=True)


df_train.Sex.replace(('male','female'),(0,1), inplace=True)
df_train.Embarked.replace(('S','C', 'Q'),(0,1,2), inplace=True)
df_train.Title.replace(('Mr', 'Mrs', 'Miss', 'Master', 'Royalty', 'Rev', 'Dr', 'Officer'),(0, 1, 2, 3, 4, 5, 6, 7), inplace=True)

# ML

y = df_train['Survived']
x = df_train.drop(['Survived', 'PassengerId'], axis=1)

x_train, x_val, y_train, y_val = train_test_split(x,y,test_size=0.1)

randomforest = RandomForestClassifier()
randomforest.fit(x_train, y_train) 
y_pred = randomforest.predict(x_val)
acc_randomforest = accuracy_score(y_pred,y_val)



# save model 
pickle.dump(randomforest, open('titanichhh_model.sav', 'wb'))


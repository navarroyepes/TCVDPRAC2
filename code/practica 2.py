#!/usr/bin/env python
# coding: utf-8

# In[60]:


# Importación de las librerias científicas
import csv 
import pandas as pd
import numpy as np
import statistics


# In[83]:


# Carga del dataset y vista general de los 30 primeros pasajeros y los últimos 5
dataset = pd.read_csv('C:/Users/andre/Desktop/Proyecto/train.csv', header=0)
dataset.tail()


# In[85]:


dataset.head(30)


# In[86]:


# eliminación de las columnas no relevantes
del dataset ['Name']

del dataset ['Cabin']

del dataset ['Ticket']

del dataset ['Fare']

del dataset ['Embarked']


# In[87]:


dataset.head()


# In[88]:


# Creación de la nueva columna gender (variable binaria) mediante condicionales
def getNumber(Sex):
    if Sex=="male":
        return 1
    else:
        return 0
dataset["Gender"]= dataset["Sex"].apply(getNumber)
dataset.head()


# In[89]:


# borramos la columna Sex porque la sustituimos por gender 
del dataset['Sex']
dataset.head()


# In[90]:


dataset.isnull()


# In[91]:


dataset.isnull().sum()


# In[92]:


dataset.describe()


# In[93]:


#aplicamos la media de edad en los pasajeros que no sobrevivieron
mean_no_survived = dataset[dataset.Survived == 0].Age.mean()
print (mean_no_survived)


# In[94]:


mean_survived = dataset[dataset.Survived == 1].Age.mean()
print (mean_survived)


# In[95]:


dataset.mean()


# In[112]:


mean_age = dataset.Age.mean()
print (mean_age)


# In[113]:


print (type ('Age'))


# In[122]:


dataset.fillna(mean_age) 


# In[123]:


dataset.head(30)


# In[ ]:





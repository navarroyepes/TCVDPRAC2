#!/usr/bin/env python
# coding: utf-8

# In[17]:


# Importación de las librerias científicas
import csv 
import pandas as pd
import numpy as np 
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
from matplotlib import style


# In[18]:


# Carga del dataset y vista general de los 30 primeros pasajeros y los últimos 5
dataset = pd.read_csv('C:/Users/andre/Desktop/Proyecto/train.csv', header=0, dtype={'Age': np.float64})
dataset.tail()


# In[19]:


dataset.head(30)


# In[20]:


# eliminación de las columnas no relevantes
del dataset ['Name']

del dataset ['Cabin']

del dataset ['Ticket']

del dataset ['Fare']

del dataset ['Embarked']


# In[21]:


dataset.head()


# In[22]:


# Creación de la nueva columna gender (variable binaria) mediante condicionales
def getNumber(Sex):
    if Sex=="male":
        return 1
    else:
        return 0
dataset["Gender"]= dataset["Sex"].apply(getNumber)
dataset.head()


# In[23]:


# borramos la columna Sex porque la sustituimos por gender 
del dataset['Sex']
dataset.head()


# In[24]:


dataset.isnull()


# In[25]:


dataset.isnull().sum()


# In[26]:


dataset.describe()


# In[27]:


#aplicamos la media de edad en los pasajeros que no sobrevivieron
mean_no_survived = dataset[dataset.Survived == 0].Age.mean()
print (mean_no_survived)


# In[28]:


mean_survived = dataset[dataset.Survived == 1].Age.mean()
print (mean_survived)


# In[29]:


dataset.mean()


# In[30]:


mean_age = dataset.Age.mean()
print (mean_age)


# In[31]:


print (type ('Age'))


# In[122]:


dataset.fillna(mean_age) 


# In[34]:


dataset.Age.plot.box(grid=True)


# In[42]:


dataset.Age.plot.box(grid=True, figsize=(10,25))


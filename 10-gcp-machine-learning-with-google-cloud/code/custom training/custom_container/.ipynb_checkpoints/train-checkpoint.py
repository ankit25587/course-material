#!/usr/bin/env python
# coding: utf-8

# # This is Custom training

# In[1]:


import pandas as pd


# In[2]:


data = pd.read_csv("gs://custom_container_training/IRIS.csv")


# In[3]:


# In[4]:

data

# In[5]:


from sklearn.model_selection import train_test_split
array = data.values
X = array[:,0:4]
y = array[:,4]
# Split the data to train and test dataset.
X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.20, random_state=1)


# In[7]:


X_train.shape


# In[8]:


X_test.shape


# In[9]:


y_train.shape


# In[10]:


y_test.shape


# In[11]:


from sklearn.svm import SVC
svn = SVC()
svn.fit(X_train, y_train)


# In[12]:


svn


# In[13]:


predictions = svn.predict(X_test)
# Calculate the accuracy 
from sklearn.metrics import accuracy_score 
accuracy_score(y_test, predictions)


# In[14]:


import pickle
import logging
with open('model.pkl', 'wb') as model_file:
  pickle.dump(svn, model_file)


# In[15]:


from google.cloud import storage
storage_path = "gs://custom_container_training/model.pkl"
blob = storage.blob.Blob.from_string(storage_path, client=storage.Client())
blob.upload_from_filename('model.pkl')
logging.info("model exported to : {}".format(storage_path))


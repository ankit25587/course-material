#!/usr/bin/env python
# coding: utf-8

# In[1]:


from  sklearn import  datasets
iris=datasets.load_iris()
x=iris.data
y=iris.target
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.5)
from sklearn import tree
classifier=tree.DecisionTreeClassifier()
classifier.fit(x_train,y_train)
predictions=classifier.predict(x_test)
from sklearn.metrics import accuracy_score
print(accuracy_score(y_test,predictions))


# In[3]:


import pickle
pkl_filename = "pickle_model.pkl"
with open(pkl_filename, 'wb') as file:
    pickle.dump(classifier, file)


# In[4]:


get_ipython().system('ls -a')


# In[5]:


from google.cloud import storage


# In[8]:


storage_client = storage.Client()


# In[16]:


bucket = storage_client.get_bucket('bigdata-255')


# In[18]:


blob = bucket.blob('model.pkl')
blob.upload_from_filename('pickle_model.pkl')


# In[15]:


import sklearn
sklearn.__version__


# In[ ]:





# In[ ]:





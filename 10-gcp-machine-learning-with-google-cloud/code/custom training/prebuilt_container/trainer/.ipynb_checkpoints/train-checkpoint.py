#!/usr/bin/env python
# coding: utf-8

# In[3]:


from keras.models import Sequential
from keras.layers import Dense
from sklearn.preprocessing import LabelEncoder
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
import numpy as np
import pandas as pd
np.random.seed(7)

import argparse
parser = argparse.ArgumentParser()

parser.add_argument( 
    '--input_data',
    type = str
)

parser.add_argument( 
    '--mod_out',
    type = str
)

args = parser.parse_args()
arguments = args.__dict__

inpute_file = arguments['input_data']
mod_out = arguments['mod_out']

#df = pd.read_csv("gs://prebuilt_container_training/IRIS.csv")
df = pd.read_csv(inpute_file)


# In[4]:


df


# In[5]:


X = df.drop(["species"],axis=1)
Y = df['species'].map({'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2})


# In[8]:


encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)

dummy_y = np_utils.to_categorical(encoded_Y)


# In[10]:


model = Sequential()
model.add(Dense(8, input_dim=4, activation='relu'))
model.add(Dense(3, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


# In[11]:


model.fit(X, dummy_y, epochs=150, batch_size=5)


# In[12]:


scores = model.evaluate(X, dummy_y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))


# In[13]:


predictions = model.predict(X)


# In[14]:


test = np.argmax(predictions,axis=1)
test


# In[15]:


#model.save('gs://prebuilt_container_training/model_output')
model.save(mod_out)


# In[ ]:





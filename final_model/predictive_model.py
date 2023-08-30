def predictor():
	#!/usr/bin/env python
	# coding: utf-8

	# In[1]:


	# import data
	import pandas as pd
	df = pd.read_csv('nigeria_houses_data.csv')


	# In[2]:


	# convert float values to integer variables
	float_cols = [col for col in df.columns if df[col].dtype == 'float64']

	for col in float_cols:
	    df[col] = df[col].astype('int64')


	# In[3]:


	# one-hot encode and ordinal encode the categorical columns
	from sklearn.preprocessing import LabelEncoder
	le = LabelEncoder()
	title_encoded = pd.get_dummies(df['title'])
	state_encoded = pd.get_dummies(df['state'])
	town_encoded = le.fit_transform(df['town'])


	# In[4]:


	# add encoded columns to dataset
	df = df.join(title_encoded)
	df = df.join(state_encoded)
	df['town_encoded'] = town_encoded


	# In[5]:


	# drop categorical data
	cat_cols = [col for col in df.columns if df[col].dtype == 'object']
	df.drop(cat_cols, axis=1, inplace=True)


	# In[6]:


	# remove outliers
	df = df[df['price']<1500000000]


	# In[7]:


	# define dependent and independent variables
	X = df.drop('price', axis=1) #independent variable
	y = df['price'] #dependent variable


	# In[8]:


	# Modeling
	# build the models
	from sklearn.svm import SVR
	from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, BaggingRegressor
	from sklearn.ensemble import VotingRegressor
	from sklearn import metrics
	seed = 2022
	boosting = GradientBoostingRegressor(random_state=seed)
	bagging = BaggingRegressor(random_state=seed)
	forest = RandomForestRegressor(max_features=0.8, n_estimators=300, min_samples_leaf=10, random_state=seed, oob_score=True, n_jobs=-1)


	# In[9]:


	estimators = [('Bagging', bagging), ('Boosting', boosting), ('Random Forests', forest)]


	# In[10]:


	predictor_model = VotingRegressor(estimators=estimators, weights=[2, 1, 2])


	# In[11]:


	predictor_model.fit(X, y)
	return predictor_model
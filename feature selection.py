# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 12:54:13 2022

@author: Demian
"""

# from sklearn.feature_selection import SelectPercentile
# from sklearn.feature_selection import chi2,f_classif
# from sklearn.datasets import load_breast_cancer

# X,y = load_breast_cancer(return_X_y=True)
# print(X.shape)
# chi_percentile = SelectPercentile(score_func=chi2,percentile=20)
# new_x = chi_percentile.fit_transform(X,y)
# print(new_x.shape)


# from sklearn.datasets import load_digits
# from sklearn.feature_selection import chi2,f_classif
# from sklearn.feature_selection import SelectPercentile

# X,y=load_digits(return_X_y=True)
# print(X.shape)

# new_features = SelectPercentile(score_func=chi2,percentile=50)
# x=new_features.fit_transform(X,y)
# print(x.shape)
# print(y.shape) 
# print(new_features.get_support()) #true for selected features 

###################################33
# from sklearn.feature_selection import chi2 , f_classif

# from sklearn.feature_selection import GenericUnivariateSelect
# from sklearn.datasets import load_boston,load_breast_cancer

# X,y = load_breast_cancer(return_X_y=(True))
# print(X.shape,'\n',y.shape)
# # print(y[:10])

# new_features = GenericUnivariateSelect(score_func=(chi2),mode='k_best',param=10)
# x=new_features.fit_transform(X,y)
# print(x.shape)
# print(new_features.get_support())


##################################################
'''
from sklearn.feature_selection import chi2,f_classif
from sklearn.feature_selection import SelectKBest
from sklearn.datasets import load_digits
x,y=load_digits(return_X_y=True)
print(x.shape)

new_features= SelectKBest(chi2,k=60)
x = new_features.fit_transform(x,y)
print(x.shape)
print(new_features.get_support())
'''
#####################################

from sklearn.feature_selection import SelectFromModel
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_breast_cancer
x,y=load_breast_cancer(return_X_y=True)
print(x.shape)

model = LinearRegression()

new_features = SelectFromModel(estimator = model)
new_x = new_features.fit_transform(x,y)
print(new_x.shape)












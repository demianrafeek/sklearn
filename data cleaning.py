# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 16:07:16 2022

@author: Demian
"""
# from sklearn.impute import SimpleImputer
# data = [[3,6,0],
#         [0,8,6],
#         [6,7,2],
#         [0,0,7],
#         [3,0,0]]
# imp = SimpleImputer(missing_values = 0 ,strategy='mean')
# print(data)
# imp = imp.fit(data)
# print(data)
# data = imp.transform(data)
# print(data)

#########################################33
from sklearn.datasets import load_breast_cancer
from sklearn.impute import SimpleImputer
import numpy as np

X,y = load_breast_cancer(return_X_y=True)
imp= SimpleImputer(missing_values = np.nan , strategy = 'median')
imp=imp.fit(X)
x = imp.transform(X)














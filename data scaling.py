# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 14:58:59 2022

@author: Demian
"""
# standard scaler  (standardization) => (x- mean)/std  => [-1,1]
from sklearn.preprocessing import StandardScaler

x=[[429,367],
   [963,945239],
   [0,742],
   [654,-741],
   [-10,0]]

scaler = StandardScaler()
new_x = scaler.fit_transform(x)
print(new_x)


# min max scaler (normalization) => (x-mean)/(max-min)  =>[0,1]

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
newx = scaler.fit_transform(x)
print(new_x)


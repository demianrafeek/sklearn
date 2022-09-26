# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 19:19:06 2022

@author: Demian
"""

import numpy as np
from sklearn.model_selection import train_test_split

x=np.arange(10).reshape((5,2))
# print(x)
y=np.arange(5)
# print(y)

# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.33,random_state=4294000000,shuffle=True)
# print(x_train)
# print(y_train)


from sklearn.model_selection import KFold

kf = KFold(n_splits=4)
print(kf.split(x))











# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 15:06:02 2022

@author: Demian
"""
# from sklearn.datasets import load_iris

# iris_data = load_iris()
# x=iris_data.data
# # print(x.shape)
# y=iris_data.target
# print("features names ", iris_data.feature_names)
# print('target names ', iris_data.target_names)

##################################################
# from sklearn.datasets import load_digits
# data = load_digits()
# x=data.data
# y=data.target

# # print(x[:1])
# print(x.shape)
# print(y.shape)

# import matplotlib.pyplot as plt
# # plt.gray()

# for i in range(10):
#     print(" imge number ", i)
#     plt.imshow(data.images[i])
#     plt.show()

##################################################

# from sklearn.datasets import load_boston
# data = load_boston()
# x=data.data
# y=data.target
# print(x.shape)
# print(data.feature_names)
# print(y.shape)
 

##################################################

# from sklearn.datasets import load_wine
# data = load_wine()
# x= data.data
# y=data.target

# print(data.feature_names)
# print('target names : \n',data.target_names)


##################################################
# from sklearn.datasets import load_breast_cancer
# data = load_breast_cancer()
# x=data.data
# y=data.target

# print(x.shape)

# print(y[:50])
# print(y.shape)
# print(data.target_names)


##################################################
# from sklearn.datasets import make_regression
# x,y = make_regression(n_samples=100,n_features=10,shuffle=True)
# print(x[:10])
# print(x.shape)

# print(y[:10])
# print(y.shape)


##################################################
from sklearn.datasets import make_classification
x,y=make_classification(n_features=10,n_samples=100,shuffle=True)
print(x.shape)
print(y.shape)










# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 20:08:57 2022

@author: Demian
"""
#####   Regrission metrics    ###########
# from sklearn.metrics import mean_absolute_error,mean_squared_error,median_absolute_error
# y_train=[3,5,1,9,7,2,4]
# y_test =[2,4,3,6,9,1,4]

# err = mean_absolute_error(y_train,y_test)
# square_err=mean_squared_error(y_train,y_test)#,multioutput='raw_values')
# median_err=median_absolute_error(y_train,y_test)
# print(err)
# print(square_err)
# print(median_err,'\n')

# y_train=[[3,4,8],
#          [2,5,7],
#          [1,6,7],
#          [3,4,8],
#          [2,6,9]]
# y_test =[[2,6,7],
#          [2,5,8],
#          [1,6,9],
#          [3,5,7],
#          [2,4,9]]
# mean_error = mean_absolute_error(y_train,y_test,multioutput='uniform_average')
# mean_square_err=mean_squared_error(y_train,y_test)
# median_error=median_absolute_error(y_train,y_test)
# print(mean_error)
# print(mean_square_err)
# print(median_error,'\n')

# mean_error2=mean_absolute_error(y_train,y_test,multioutput='raw_values')
# mean_square_error2=mean_squared_error(y_train,y_test,multioutput='raw_values')
# median_error2=median_absolute_error(y_train,y_test)
# print(mean_error2) # calc error in each coloumn
# print(mean_square_error2)
# print(median_error2)


######  classificationmetrics   ################

import seaborn as sns
from sklearn.metrics import confusion_matrix
y_true = ['a','a','b','a','a','b','b','b']
y_pred = ['a','b','b','a','a','b','a','a']

# #confusion matrix
# cm=confusion_matrix(y_true,y_pred) TP FN  FP TN
# print(cm)
# sns.heatmap(cm)


# #accuracy score = (TP+TN)/(TP+TN+FP+FN)  with normaliaztion 
# from sklearn.metrics import accuracy_score
# acc = accuracy_score(y_true,y_pred,normalize=True) #5/8
# print(acc)
# acc2 = accuracy_score(y_true,y_pred,normalize=False) # 5 
# print(acc2)


# # recall (sensitivity) = TP/(TP + FN)  المرضي الحقيقيين 
# from sklearn.metrics import recall_score
# recall = recall_score(y_true,y_pred,pos_label='b')
# print(recall)


# # precision (specificity) = TP / (TP + FP) المرضي اللي توقعهم 
# from sklearn.metrics import precision_score
# precision = precision_score(y_true,y_pred,pos_label='b')
# print(precision)


# # f1 score  = 2*(precision * recall)/(precision + recall)
# from sklearn.metrics import f1_score
# f1 = f1_score(y_true,y_pred,average='micro') # averag => macro , binary 
# print(f1)
# print(2*recall*precision/(recall+precision))


# classification report
from sklearn.metrics import classification_report
cr=classification_report(y_true,y_pred)
print(cr)












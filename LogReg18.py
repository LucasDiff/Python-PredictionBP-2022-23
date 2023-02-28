#implementacia Logistickej regresie s 18 parametrami

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt
from pylab import rcParams
import urllib
import sklearn
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score, KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedGroupKFold
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn import metrics
from xgboost import XGBRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler,MinMaxScaler,RobustScaler,MaxAbsScaler

#naci­tanie dat :
predictdatafinal = pd.read_csv('data\predictdataoldfinal.txt')

#predspracovanie dat :
ohe = OneHotEncoder()

#encode = np.array(predictdatafinal["team1ranking"]).reshape(-1, 1)

#one_hot_encoder = ohe.fit(encode)
#ohe_coded = ohe.transform(encode).toarray() 
predictdatafinal["team1ranking"] = predictdatafinal["team1ranking"] * 10
predictdatafinal["team2ranking"] = predictdatafinal["team2ranking"] * 10
predictdatafinal = predictdatafinal.drop(columns=["Unnamed: 0"])
#predictdatafinal = predictdatafinal.drop(columns=["team1ranking"])  

#predictdatafinal["team1rankingS+"] = ohe_coded[:,0]   
#predictdatafinal["team1rankingS"] = ohe_coded[:,1]
#predictdatafinal["team1rankingA"] = ohe_coded[:,2]
#predictdatafinal["team1rankingB"] = ohe_coded[:,3]  
#predictdatafinal["team1rankingC"] = ohe_coded[:,4]
#predictdatafinal["team1rankingD"] = ohe_coded[:,5]

#bb = np.array(predictdatafinal["team2ranking"]).reshape(-1, 1)

#one_hot_encoder = ohe.fit(bb)
#ohe_coded = ohe.transform(bb).toarray() 

#predictdatafinal = predictdatafinal.drop(columns=["team2ranking"])  

#predictdatafinal["team2rankingS+"] = ohe_coded[:,0]  
#predictdatafinal["team2rankingS"] = ohe_coded[:,1]
#predictdatafinal["team2rankingA"] = ohe_coded[:,2]
#predictdatafinal["team2rankingB"] = ohe_coded[:,3]   
#predictdatafinal["team2rankingC"] = ohe_coded[:,4]
#predictdatafinal["team2rankingD"] = ohe_coded[:,5]

cc = np.array(predictdatafinal["winner"]).reshape(-1, 1)

one_hot_encoder = ohe.fit(cc)
ohe_coded = ohe.transform(cc).toarray() 

predictdatafinal = predictdatafinal.drop(columns=["winner"]) 

predictdatafinal["winner"] = ohe_coded[:,0]   

X = predictdatafinal.iloc[:, :-1].values
y = predictdatafinal.iloc[:, 10].values

scaler = MaxAbsScaler()
scaler.fit(X)
X= scaler.transform(X)




#vyhodnotenie + grid search
#grid_search_params = {
#    'penalty' : [ 'l2'],
#    'solver' : ['newton-cg', 'lbfgs'],
#    'warm_start' : [0,1],
#    'multi_class' : ['auto', 'ovr']
#    }
#gs = GridSearchCV(LogReg, grid_search_params, cv = 10, scoring="accuracy")
#gs.fit(X,y)

#print("Najlepsie parametre:",gs.best_estimator_)
#print("Skore :",gs.best_score_)


# Cross-validation with Logistic Regression model
LogRegs = LogisticRegression(solver='newton-cg', warm_start=0)
scores = cross_val_score(LogRegs, X, y, cv=10)

# Load the new data to be checked
new_data = pd.read_csv('output8.txt')
new_data = new_data.drop(columns=["Unnamed: 0"])

# Scale the new data
X_new = new_data.values
X_new = scaler.transform(X_new)

# Predict class probabilities for new data
num_predictions = 100
total_prediction = 0
for i in range(num_predictions):
    LogRegs.fit(X, y)
    y_prob = LogRegs.predict_proba(X_new)[:, 1]
    total_prediction += y_prob

average_prediction = total_prediction / num_predictions
if (average_prediction >= 0.5):
    print("Team 1/ONE is going to win on average.")
else:
    print("Team 2/TWO is going to win on average.")

print("Cross-validation score: {:.2f} +/- {:.2f}".format(scores.mean(), scores.std()))
print(average_prediction)
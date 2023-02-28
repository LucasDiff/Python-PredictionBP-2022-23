#implementácia k najbližších susedov s 32 parametrami

import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt
from pylab import rcParams
import urllib
import sklearn
from sklearn.preprocessing import OneHotEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn import neighbors
from sklearn import tree, model_selection
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score, KFold
from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler,MinMaxScaler,RobustScaler,MaxAbsScaler
from sklearn import utils
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.model_selection import GridSearchCV
import scipy.stats as st


# import warnings filter
from warnings import simplefilter
# ignore all future warnings
simplefilter(action='ignore', category=FutureWarning)


#načítanie dát :
predictdatanew = pd.read_csv('data\predictdatanew.txt')
predictdatanew = predictdatanew.drop(columns=["Unnamed: 0"])
X = predictdatanew.iloc[:, :-1].values
y = predictdatanew.iloc[:, 32].values


def custom_weights(distances):
    weights = np.zeros(distances.shape)
    weights[:, [0, 6]] = 1  # give more weight to team1ranking and team2ranking
    return weights


#predspracovanie dát :
scaler = MinMaxScaler()
scaler.fit(X)
X= scaler.transform(X)

#trénovanie modelu :
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
classifier = KNeighborsClassifier(n_neighbors=40, weights='distance')
classifier.fit(X_train, y_train)

scores = cross_val_score(classifier, X, y, cv=10)


# load new data to be checked
new_data = pd.read_csv('output32.txt')
new_data = new_data.drop(columns=["Unnamed: 0"])

# Scale the new data
X_new = new_data.values
X_new = scaler.transform(X_new)

num_predictions = 300
total_prediction = 0
total_winrate = 0
for i in range(num_predictions):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    classifier = KNeighborsClassifier(n_neighbors=40)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_new)
    total_prediction += y_pred
average_prediction = total_prediction / num_predictions
average_prediction = average_prediction.mean()
if (average_prediction >= 0.5):
    print("Team 1/ONE is going to win on average.")
else:
    print("Team 2/TWO is going to win on average.")

total_winrate = total_winrate + average_prediction
winrate1 = average_prediction
print("Cross-validation score: {:.2f} +/- {:.2f}".format(scores.mean(), scores.std()))
print(average_prediction)












#nacitanie dat :
predictdatafinal = pd.read_csv('data\predictdatafinal.txt')

#predspracovanie dat :
ohe = OneHotEncoder()

aa = np.array(predictdatafinal["team2ranking"]).reshape(-1, 1)

one_hot_encoder = ohe.fit(aa)
ohe_coded = ohe.transform(aa).toarray() 




predictdatafinal["team1rankingSS"] = ohe_coded[:,0]   
predictdatafinal["team1rankingS"] = ohe_coded[:,1]
predictdatafinal["team1rankingA"] = ohe_coded[:,2]
predictdatafinal["team1rankingB"] = ohe_coded[:,3]  
predictdatafinal["team1rankingC"] = ohe_coded[:,4]
predictdatafinal["team1rankingD"] = ohe_coded[:,5]

bb = np.array(predictdatafinal["team1ranking"]).reshape(-1, 1)

one_hot_encoder = ohe.fit(bb)
ohe_coded = ohe.transform(bb).toarray() 

predictdatafinal = predictdatafinal.drop(columns=["team2ranking"]) 
predictdatafinal = predictdatafinal.drop(columns=["team1ranking"])  

predictdatafinal["team2rankingSS"] = ohe_coded[:,0] 
predictdatafinal["team2rankingS"] = ohe_coded[:,1]
predictdatafinal["team2rankingA"] = ohe_coded[:,2]
predictdatafinal["team2rankingB"] = ohe_coded[:,3]  
predictdatafinal["team2rankingC"] = ohe_coded[:,4]
predictdatafinal["team2rankingD"] = ohe_coded[:,5]




#encode = np.array(predictdatafinal["team1ranking"]).reshape(-1, 1)

#one_hot_encoder = ohe.fit(encode)
#ohe_coded = ohe.transform(encode).toarray() 

predictdatafinal = predictdatafinal.drop(columns=["Unnamed: 0"])

cc = np.array(predictdatafinal["winner"]).reshape(-1, 1)

one_hot_encoder = ohe.fit(cc)
ohe_coded = ohe.transform(cc).toarray() 

predictdatafinal = predictdatafinal.drop(columns=["winner"]) 

predictdatafinal["winner"] = ohe_coded[:,0]  

X = predictdatafinal.iloc[:, :-1].values
y = predictdatafinal.iloc[:, 44].values



scaler = MaxAbsScaler()
scaler.fit(X)
X= scaler.transform(X)




# Cross-validation with Logistic Regression model
LogReg = LogisticRegression(solver='newton-cg', warm_start=0)
scores = cross_val_score(LogReg, X, y, cv=10)

# Load the new data to be checked
new_data = pd.read_csv('output.txt')
new_data = new_data.drop(columns=["Unnamed: 0"])

# Scale the new data
X_new = new_data.values
X_new = scaler.transform(X_new)



# Predict class probabilities for new data
num_predictions = 300
total_prediction = 0
for i in range(num_predictions):
    LogReg.fit(X, y)
    y_prob = LogReg.predict_proba(X_new)[:, 1]
    total_prediction += y_prob

average_prediction = total_prediction / num_predictions
if (average_prediction >= 0.5):
    print("Team 1/ONE is going to win on average.")
else:
    print("Team 2/TWO is going to win on average.")

print("Cross-validation score: {:.2f} +/- {:.2f}".format(scores.mean(), scores.std()))
print(average_prediction)

total_winrate = total_winrate + average_prediction 
winrate2 = average_prediction
average_prediction = 0











#naci­tanie dat :
predictdatafinal = pd.read_csv('data\predictdataoldfinal.txt')

#predspracovanie dat :
ohe = OneHotEncoder()

aa = np.array(predictdatafinal["team2ranking"]).reshape(-1, 1)

one_hot_encoder = ohe.fit(aa)
ohe_coded = ohe.transform(aa).toarray() 





predictdatafinal["team1rankingSS"] = ohe_coded[:,0]   
predictdatafinal["team1rankingS"] = ohe_coded[:,1]
predictdatafinal["team1rankingA"] = ohe_coded[:,2]
predictdatafinal["team1rankingB"] = ohe_coded[:,3]  
predictdatafinal["team1rankingC"] = ohe_coded[:,4]
predictdatafinal["team1rankingD"] = ohe_coded[:,5]

bb = np.array(predictdatafinal["team1ranking"]).reshape(-1, 1)

one_hot_encoder = ohe.fit(bb)
ohe_coded = ohe.transform(bb).toarray() 

predictdatafinal = predictdatafinal.drop(columns=["team2ranking"]) 
predictdatafinal = predictdatafinal.drop(columns=["team1ranking"])  

predictdatafinal["team2rankingSS"] = ohe_coded[:,0] 
predictdatafinal["team2rankingS"] = ohe_coded[:,1]
predictdatafinal["team2rankingA"] = ohe_coded[:,2]
predictdatafinal["team2rankingB"] = ohe_coded[:,3]  
predictdatafinal["team2rankingC"] = ohe_coded[:,4]
predictdatafinal["team2rankingD"] = ohe_coded[:,5]




#encode = np.array(predictdatafinal["team1ranking"]).reshape(-1, 1)

#one_hot_encoder = ohe.fit(encode)
#ohe_coded = ohe.transform(encode).toarray() 

predictdatafinal = predictdatafinal.drop(columns=["Unnamed: 0"])


cc = np.array(predictdatafinal["winner"]).reshape(-1, 1)

one_hot_encoder = ohe.fit(cc)
ohe_coded = ohe.transform(cc).toarray() 

predictdatafinal = predictdatafinal.drop(columns=["winner"]) 

predictdatafinal["winner"] = ohe_coded[:,0]   

X = predictdatafinal.iloc[:, :-1].values
y = predictdatafinal.iloc[:, 20].values

scaler = MaxAbsScaler()
scaler.fit(X)
X= scaler.transform(X)




# Cross-validation with Logistic Regression model
LogRegs = LogisticRegression(solver='newton-cg', warm_start=0)
scores = cross_val_score(LogRegs, X, y, cv=10)

# Load the new data to be checked
new_data = pd.read_csv('output20.txt')
new_data = new_data.drop(columns=["Unnamed: 0"])

# Scale the new data
X_new = new_data.values
X_new = scaler.transform(X_new)

# Predict class probabilities for new data
num_predictions = 300
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

total_winrate = total_winrate + average_prediction 
winrate3 = average_prediction
average_prediction = 0

total_winrate = total_winrate / 3
print("\n After all calculations :")
if (total_winrate >= 0.5):
    print("Team 1/ONE is going to win on average.")
else:
    print("Team 2/TWO is going to win on average.")
print("Total winrate : ", total_winrate)

winrate2_float = float(winrate2)
winrate3_float = float(winrate3)
total_winrate_float = float(total_winrate)
winrate2 = winrate2_float

winrate3 = winrate3_float
total_winrate = total_winrate_float
datas3 = {'winrate1': [winrate1], 
        'winrate2': [winrate2],
        'winrate3': [winrate3],
        'total_winrate': [total_winrate]
}
data_frameee = pd.DataFrame(datas3)
data_frameee.to_csv('output4.txt')




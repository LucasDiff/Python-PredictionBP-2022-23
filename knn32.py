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

#načítanie dát :
predictdatanew = pd.read_csv('data\predictdatanew.txt')
predictdatanew = predictdatanew.drop(columns=["Unnamed: 0"])
X = predictdatanew.iloc[:, :-1].values
y = predictdatanew.iloc[:, 32].values

#predspracovanie dát :
scaler = MinMaxScaler()
scaler.fit(X)
X= scaler.transform(X)

#trénovanie modelu :
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
classifier = KNeighborsClassifier(n_neighbors=40, weights='distance')
classifier.fit(X_train, y_train)

scores = cross_val_score(classifier, X, y, cv=10)
#vyhodnotenie + grid search
#grid_search_params = {
#    'n_neighbors' : [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,25,30,35,40,45,50],
#    'weights' : ['uniform','distance'],
#    'algorithm' : ['auto','ball_tree','kd_tree','brute']
#    }
#gs = GridSearchCV(classifier, grid_search_params, cv = 10, scoring="accuracy")
#gs.fit(X,y)

#print("Najlepšie parametre:",gs.best_estimator_)
#print("Skóre :",gs.best_score_)


# load new data to be checked
new_data = pd.read_csv('output32.txt')
new_data = new_data.drop(columns=["Unnamed: 0"])

# Scale the new data
X_new = new_data.values
X_new = scaler.transform(X_new)

num_predictions = 10
total_prediction = 0
for i in range(num_predictions):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
    classifier = KNeighborsClassifier(n_neighbors=40, weights='distance')
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_new)
    total_prediction += y_pred

average_prediction = total_prediction / num_predictions
average_prediction = average_prediction.mean()
if (average_prediction >= 0.5):
    print("Team 1/ONE is going to win on average.")
else:
    print("Team 2/TWO is going to win on average.")

print("Cross-validation score: {:.2f} +/- {:.2f}".format(scores.mean(), scores.std()))
print(average_prediction)

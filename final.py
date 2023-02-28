import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MaxAbsScaler
from sklearn.svm import SVC
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


# Load the training data
predictdatanew = pd.read_csv('trainingdata.txt')
predictdatanew = predictdatanew.drop(columns=["Unnamed: 0"])

# Add a new column with the average of the first three columns
predictdatanew['total_winrate'] = predictdatanew.iloc[:, :3].mean(axis=1)

# Divide the average column by 3
predictdatanew['total_winrate'] = predictdatanew['total_winrate'] / 3

X = predictdatanew.iloc[:, [0, 1, 2, 4]].values
y = predictdatanew.iloc[:, 3].values

# Preprocess the data
scaler = MaxAbsScaler()
scaler.fit(X)
X = scaler.transform(X)

# Train the classifier
classifier = KNeighborsClassifier(n_neighbors=25)
classifier.fit(X, y)

# Load the new data to be checked
new_data = pd.read_csv('output4.txt')
new_data = new_data.drop(columns=["Unnamed: 0"])

# Scale the new data
X_new = scaler.transform(new_data.values)

# Predict the class probabilities for new data
num_predictions = 10000
total_prediction = 0
for i in range(num_predictions):
    y_prob = classifier.predict_proba(X_new)[:, 1]
    total_prediction += y_prob
average_prediction = total_prediction / num_predictions
winrate = average_prediction.mean()

if (winrate >= 0.5):
    print("Team 1/ONE is going to win on average.")
else:
    print("Team 2/TWO is going to win on average.")
    
print(f"Average win rate: {winrate}")



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
LogReg = LogisticRegression(solver='newton-cg',warm_start = 0)
LogReg.fit(X_train, y_train)





X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
svclassifier = SVC( probability = 1, gamma='auto', verbose = 0, break_ties = 0)
svclassifier.fit(X_train, y_train)

# Predict the class probabilities for new data
num_predictions = 10000
total_prediction = 0
for i in range(num_predictions):
    y_prob = svclassifier.predict_proba(X_new)[:, 1]
    total_prediction += y_prob
average_prediction = total_prediction / num_predictions
winrate = average_prediction.mean()

if (winrate >= 0.5):
    print("Team 1/ONE is going to win on average.")
else:
    print("Team 2/TWO is going to win on average.")
    
print(f"Average win rate: {winrate}")


# Predict the class probabilities for new data
num_predictions = 10000
total_prediction = 0
for i in range(num_predictions):
    y_prob = LogReg.predict_proba(X_new)[:, 1]
    total_prediction += y_prob
average_prediction = total_prediction / num_predictions
winrate = average_prediction.mean()

if (winrate >= 0.5):
    print("Team 1/ONE is going to win on average.")
else:
    print("Team 2/TWO is going to win on average.")
    
print(f"Average win rate: {winrate}")




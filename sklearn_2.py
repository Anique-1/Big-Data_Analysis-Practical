import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score



x, y=load_iris(return_X_y=True)



model=LogisticRegression()
x_train, X_test, y_train, y_test=train_test_split(x, y, test_size=0.2)
# cross=cross_val_score(model, x, y, cv=10)
# print(cross.mean())
# print(cross.std())









#features selection bias parameters
#cross validation
# This code snippet is performing the following tasks:
model=[ LogisticRegression(max_iter=1000), DecisionTreeClassifier(), KNeighborsClassifier(), RandomForestClassifier(),GaussianNB(), SVC()]
def cross_valid():
    for models in model:
        cross_validstion= cross_val_score(models, x, y, cv=10)
        print(models.__class__.__name__)
        print(round(cross_validstion.mean()*100))
        print(round(cross_validstion.std()*100))
        print("-----------------------")
cross_valid()
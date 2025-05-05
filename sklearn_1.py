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


x,y= load_iris(return_X_y=True)
#print(x)
#print(y)

x_train,x_test, y_train, y_test=train_test_split(x,y,test_size=0.2)
# print(x_train.shape)
# print(x_test.shape)


model=DecisionTreeClassifier()
model1=KNeighborsClassifier()
model2=LogisticRegression()
model3=SVC()
model3.fit(x_train,y_train)

avc=model3.predict(x_test)
avc1=accuracy_score(avc,y_test)
# print(avc1)


model=[ LogisticRegression(), DecisionTreeClassifier(), KNeighborsClassifier(), RandomForestClassifier(),GaussianNB()]
def compare_model():
    for models in model:
        models.fit(x_train,y_train)
        y_pred=models.predict(x_test)
        accuracy=accuracy_score(y_test, y_pred)
        print(accuracy)
compare_model()
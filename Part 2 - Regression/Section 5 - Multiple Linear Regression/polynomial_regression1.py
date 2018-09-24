#Polynomial Regression

#Data preprocessing

#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[: , 1:2].values
Y = dataset.iloc[: , 2].values

"""Missing data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN' , strategy = 'mean', axis = 0 )
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])"""

"""Encoding categorical data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,0]=labelencoder_X.fit_transform(X[:,0])
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
labelencoder_Y = LabelEncoder()
Y=labelencoder_Y.fit_transform(Y)"""

#Splitting the dataset into the Training set and Test set
"""from sklearn.cross_validation import train_test_split 
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2,random_state = 0)"""

#Feature scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""

#Fitting linear regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,Y)

#Fitting polynomial regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree = 4)
X_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly,Y)

#Visualising the linear regression results
plt.scatter(X, Y, color ='red')
plt.plot(X, lin_reg.predict(X), color ='blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

#Visualising the polynomial regression results

plt.scatter(X, Y, color ='red')
plt.plot(X, lin_reg_2.predict(poly_reg.fit_transform(X)), color ='blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

#Predicting a new result with linear regression
lin_reg.predict(6.5)

#Predicting a new result with polynomial regression
lin_reg_2.predict(poly_reg.fit_transform(6.5))
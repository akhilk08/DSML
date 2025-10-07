import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
diabetes=load_diabetes()
print("Feature names in diabetes dataset:\n",diabetes.feature_names)
diabetes_X,diabetes_y=load_diabetes(return_X_y=True)
diabetes_X=diabetes_X[:,[ 2,3,4]]
print("\nShape of BMI feature matrix:",diabetes_X.shape)
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
diabetes_y_train = diabetes_y[:-20]
diabetes_y_test = diabetes_y[-20:]
model = LinearRegression()
model.fit(diabetes_X_train, diabetes_y_train)
diabetes_y_pred = model.predict(diabetes_X_test)
bmi = float(input("\nEnter BMI value: "))
bp = float(input("Enter Blood Pressure value: "))
s1 = float(input("Enter S1 value: "))
input_array = np.array([[bmi, bp, s1]])
predicted_target = model.predict(input_array)

print(f"Predicted target variable for entered BMI: {predicted_target[0]}")

print("\nModel Coefficients:",model.coef_)
print("Model Intercept:", model.intercept_)

print("\nMean squared error: %.2f" % mean_squared_error(diabetes_y_test, diabetes_y_pred))

print("coefficient of determination(R2):%.2f"%r2_score(diabetes_y_test,diabetes_y_pred))

from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import numpy as np
import pandas as pd
import plotly.express as px

df = pd.read_csv("cleaned_data.csv")

# predict wins
X = df.drop(columns=['wins', 'name'])
y = df['wins']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# KNN Regression
knn = KNeighborsRegressor(2)
knn.fit(X_train, y_train)
KNN_prediction = knn.predict(X_test)
print(f"knn: {knn.score(X_test, y_test)}")

# Linear Regression
linear_regression_model = LinearRegression()
linear_regression_model.fit(X_train, y_train)
linear_regression_model_prediction = linear_regression_model.predict(X_test)
print(f"linear_regression_model: {linear_regression_model.score(X_test, y_test)}")

# Random Forest
gs = GridSearchCV(RandomForestRegressor(random_state=1, max_features=.5), param_grid={'n_estimators': range(10, 300, 10)})
gs.fit(X_train, y_train)
rf_prediction = gs.predict(X_test)
print(f"rf: {gs.score(X_test, y_test)}")

print(mean_absolute_error(y_test, KNN_prediction))
print(mean_absolute_error(y_test, linear_regression_model_prediction))
print(mean_absolute_error(y_test, rf_prediction))

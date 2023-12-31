# -*- coding: utf-8 -*-
"""Untitled25.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xs0HnDPii2aPmR2RaPT5bq5bwOZnAOT2

IRIS FLOWER CLASSIFICATION
"""

# Importing the libraries
import plotly.express as px
from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

""" Data Preparation and Exploration:"""

# Loading Iris dataset
data = load_iris()
IRIS = pd.read_csv("IRIS.csv")
IRIS.head()
iris_df = pd.DataFrame(data.data, columns=data.feature_names)
iris_df['species'] = data.target_names[data.target]

# Visualization the data in 3D
fig = px.scatter_3d(iris_df, x='sepal length (cm)', y='sepal width (cm)', z='petal length (cm)', color='species')
fig.show()

""" Machine Learning Model:"""

# Spliting data into features and target variable
X = iris_df.drop('species', axis=1)
y = iris_df['species']

# Spliting data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Doing Predictions
predictions = clf.predict(X_test)

# Calculating the accuracy
accuracy = accuracy_score(y_test, predictions)
print(f'Accuracy: {accuracy:.2f}')

""" Interactive 3D Scatter Plot with Predictions:"""

# Predicting species for all data points
iris_df['predicted_species'] = clf.predict(X)

# Visualize the data in 3D with predictions
fig = px.scatter_3d(iris_df, x='sepal length (cm)', y='sepal width (cm)', z='petal length (cm)',
                    color='predicted_species', symbol='species', opacity=0.6, size_max=10)

# Update the layout for better visualization
fig.update_layout(scene=dict(xaxis_title='Sepal Length', yaxis_title='Sepal Width', zaxis_title='Petal Length'))
fig.show()
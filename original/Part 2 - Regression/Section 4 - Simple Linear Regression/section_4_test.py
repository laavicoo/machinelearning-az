#Regresion Lineal Simple

#Importar librerias
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Importar el DataSet
# Importar el data set
dataset = pd.read_csv('c:/Users/barba/Documents/cursos-udemy/machinelearning-az/original/Part 2 - Regression/Section 4 - Simple Linear Regression/Salary_Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# Dividir el data set en conjunto de entrenamiento y conjunto de testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)
print (X_test)
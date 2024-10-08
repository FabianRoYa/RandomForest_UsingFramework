# -*- coding: utf-8 -*-
"""RandomForest_usando_Framework.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iHJgE1OxN1NzDJhAMBwmeQ-s7lEkz5P1
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Manual train-test split function
def manual_train_test_split(X, y, test_size=0.3, random_state=None):
    if random_state is not None:
        np.random.seed(random_state)
    indices = np.arange(X.shape[0])
    np.random.shuffle(indices)
    test_size = int(len(indices) * test_size)
    test_indices = indices[:test_size]
    train_indices = indices[test_size:]
    X_train, X_test = X[train_indices], X[test_indices]
    y_train, y_test = y[train_indices], y[test_indices]
    return X_train, X_test, y_train, y_test

# Cargar el dataset
df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/bank_preprocessed.csv')

# Preparar las características y la variable objetivo
X = df.drop(columns=['y']).values
y = np.where(df['y'] == 'yes', 1, 0)
X = X.astype(np.float64)

# Realizar la división manual en entrenamiento y prueba
X_train, X_test, y_train, y_test = manual_train_test_split(X, y, test_size=0.3, random_state=0)

# Inicializar y entrenar el modelo Random Forest
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=0)
rf_classifier.fit(X_train, y_train)

# Hacer predicciones en los datos de prueba
y_pred_test = rf_classifier.predict(X_test)

# Calcular precisión
accuracy_test = accuracy_score(y_test, y_pred_test)
print(f"Precisión en los datos de prueba: {accuracy_test}")

import seaborn as sns
from sklearn.metrics import ConfusionMatrixDisplay

# Matriz de confusión normalizada
conf_matrix_norm = confusion_matrix(y_test, y_pred_test, normalize='true')

# Gráfico de la matriz de confusión normalizada
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix_norm, annot=True, fmt='.2%', cmap='Blues')
plt.title('Matriz de Confusión')
plt.xlabel('Predicción')
plt.ylabel('Verdad')
plt.show()


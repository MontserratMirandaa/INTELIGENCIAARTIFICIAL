# Importamos las librerías necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Cargamos el conjunto de datos Iris
iris = load_iris()
X = iris.data
y = iris.target

# Dividimos el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Escalamos los datos (esto es importante para KNN)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Definimos el clasificador KNN
knn = KNeighborsClassifier(n_neighbors=3)

# Entrenamos el clasificador con los datos de entrenamiento
knn.fit(X_train, y_train)

# Realizamos predicciones con los datos de prueba
y_pred = knn.predict(X_test)

# Evaluamos el rendimiento del clasificador
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión del clasificador: {accuracy:.2f}")

# Mostramos un informe de clasificación detallado
print("Informe de clasificación:")
print(classification_report(y_test, y_pred))

# Matriz de confusión
print("Matriz de confusión:")
print(confusion_matrix(y_test, y_pred))

# Visualización (opcional)
# Visualizamos los datos y las predicciones (solo para las dos primeras características)
plt.figure(figsize=(8, 6))
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, marker='o', label='Actual')
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, marker='x', label='Predicho')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.title('KNN - Clasificación del conjunto de datos Iris')
plt.legend()
plt.show()

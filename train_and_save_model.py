# File: train_and_save_model.py
#
# This script loads the Iris dataset, trains a K-Nearest Neighbors (KNN)
# classifier, and saves the trained model to 'model.joblib' for use by the API.

import joblib
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier

# 1. Load the Iris dataset (included with scikit-learn)
iris = load_iris()
X = iris.data
y = iris.target

# 2. Initialize and train the model (using all data for simplicity in deployment)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

# 3. Save the trained model to the required file name
joblib.dump(knn, 'model.joblib')

print("Successfully trained and saved the model to 'model.joblib'.")

import os
import pandas as pd
import joblib
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler

# Load dataset
print("Loading dataset...")
df = pd.read_csv("UNSW_NB15_training-set.csv")

# Separate features and target
X = df.drop(columns=['id', 'label', 'attack_cat'], errors='ignore')
y = df['label']

# Convert categorical columns to numeric (One-Hot Encoding)
X = pd.get_dummies(X)

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train models
print("Training KMeans...")
kmeans = KMeans(n_clusters=2, random_state=42).fit(X_scaled)

print("Training KNN...")
knn = KNeighborsClassifier(n_neighbors=5).fit(X_scaled, y)

print("Training Naive Bayes...")
nb = GaussianNB().fit(X_scaled, y)

# Save models
os.makedirs("models", exist_ok=True)
joblib.dump(kmeans, "models/kmeans_model.pkl")
joblib.dump(knn, "models/knn_model.pkl")
joblib.dump(nb, "models/naive_bayes_model.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print(" All models saved in 'models/' folder")

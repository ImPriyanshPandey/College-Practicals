import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.metrics import silhouette_score

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Partitioning (K-means clustering)
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans_labels = kmeans.fit_predict(X)

# Hierarchical clustering
agg_clustering = AgglomerativeClustering(n_clusters=3)
agg_labels = agg_clustering.fit_predict(X)

# Density-based clustering (DBSCAN)
dbscan = DBSCAN(eps=0.5, min_samples=5)
dbscan_labels = dbscan.fit_predict(X)

# Evaluate cluster quality using silhouette score
kmeans_score = silhouette_score(X, kmeans_labels)
agg_score = silhouette_score(X, agg_labels)
dbscan_score = silhouette_score(X, dbscan_labels)

print(f" \nK-means Silhouette Score: {kmeans_score}")
print(f" \nHierarchical Silhouette Score: {agg_score}")
print(f" \nDBSCAN Silhouette Score: {dbscan_score}\n")

import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.svm import OneClassSVM

# Load the dataset
data = pd.read_csv("iris.csv", encoding='latin-1')

# Extract the numerical columns for outlier detection
numerical_cols = data.select_dtypes(include=np.number).columns

# Z-score method
z_scores = ((data[numerical_cols] - data[numerical_cols].mean()) / data[numerical_cols].std()).abs()
outliers_zscore = data[z_scores > 3].any(axis=1)

# IQR (Interquartile Range) method
Q1 = data[numerical_cols].quantile(0.25)
Q3 = data[numerical_cols].quantile(0.75)
IQR = Q3 - Q1
outliers_iqr = data[((data[numerical_cols] < (Q1 - 1.5 * IQR)) | (data[numerical_cols] > (Q3 + 1.5 * IQR))).any(axis=1)]

# Isolation Forest
clf_isoforest = IsolationForest(contamination=0.1)
outliers_isoforest = data[clf_isoforest.fit_predict(data[numerical_cols]) == -1]

# Local Outlier Factor (LOF)
clf_lof = LocalOutlierFactor(n_neighbors=20, contamination=0.1)
outliers_lof = data[clf_lof.fit_predict(data[numerical_cols]) == -1]

# One-Class SVM
clf_oneclasssvm = OneClassSVM(nu=0.1)
outliers_oneclasssvm = data[clf_oneclasssvm.fit_predict(data[numerical_cols]) == -1]

# Compare the performance
print(f"\nNumber of outliers detected by Z-score method:", len(outliers_zscore))
print(f"\nNumber of outliers detected by IQR method:", len(outliers_iqr))
print(f"\nNumber of outliers detected by Isolation Forest:", len(outliers_isoforest))
print(f"\nNumber of outliers detected by Local Outlier Factor:", len(outliers_lof))
print(f"\nNumber of outliers detected by One-Class SVM:", len(outliers_oneclasssvm))

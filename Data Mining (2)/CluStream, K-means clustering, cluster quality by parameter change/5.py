import pandas as pd
import numpy as np 
from sklearn.cluster import KMeans, kmeans_plusplus
from sklearn.metrics import silhouette_score
from matplotlib import pyplot as plt
import warnings

#=================Filter out all warnings==========================#
warnings.filterwarnings("ignore")
#====================load data from CSV============================#
df=pd.read_csv('AirPassengers.csv',parse_dates=['Month'],index_col='Month')
#====================Normalize the data============================#
df_normalized=(df-df.mean())/df.std()
#=================Perform KMeans Clustering========================#
kmeans=KMeans(n_clusters=3,random_state=0)
df['Cluster']=kmeans.fit_predict(df_normalized)
#===================Plot K-Means result============================#
plt.figure(figsize=(10,5))
plt.plot(df.index,df['#Passengers'],label='Passengers')
plt.scatter(df.index,df['#Passengers'],c=df['Cluster'],cmap = 'viridis',label='clusters')
plt.title('K-Means Clustering on Airline Passengers')
plt.legend()
plt.show()
#=========Calculate silhouette score for K-Means===================#
score_kmeans=silhouette_score(df_normalized,df['Cluster'])
print(f'Silhouette Score for K-Means: {score_kmeans: .2f}')
#==Simulating CluStream with K-Means by processing data in chunks==#
chunk_size=12 # Monthly Data 
scores=[]
for start in range(0,len(df),chunk_size):
    end=start+chunk_size
    chunk=df_normalized.iloc[start:end]
    if not chunk.empty:
        kmeans=KMeans(n_clusters=5,random_state=0)
        chunk_labels=kmeans.fit_predict(chunk)
        score=silhouette_score(chunk,chunk_labels)
        scores.append(score)
#=========Average silhouette score across all chunks===============#
average_score=np.mean(scores)
print(f'Average silhouette score for simulated CluStream : {average_score: .2f}')


# Importing Modules

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from tqdm import tqdm
import pickle


def kmeans_model(songs_db, **kwargs):

    # Selecting the features and scaling them

    audiofeatures = song_db.iloc[:, 3:]
    scaler = StandardScaler()
    scaler.fit(audiofeatures)
    X_scaled = scaler.transform(audiofeatures)
    audiofeatures_scaled = pd.DataFrame(X_scaled, columns=audiofeatures.columns)


    # Clustering the songs with the audio features

    kmeans = KMeans(n_clusters=)







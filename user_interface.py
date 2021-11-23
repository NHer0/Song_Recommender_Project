# Importing

import pandas as pd
import numpy as np
from hot_recommender import hot_recommender

# Loading the songs data
billboard100 = pd.read_csv(filepath_or_buffer = "Data/billboard100.csv")
hot_songs = np.array(billboard100["song"])


# First Prototype, only hot recommender
hot_recommender(hot_songs)


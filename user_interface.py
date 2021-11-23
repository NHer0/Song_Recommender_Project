# Importing

import pandas as pd
import numpy as np
from hot_recommender import hot_recommender
from billboard100_scrapper import billboard100_scrapper

# Loading the songs data

try:

    billboard100 = pd.read_csv(filepath_or_buffer="Data/billboard100.csv")

except(FileNotFoundError):

    billboard100 = billboard100_scrapper()


# First Prototype, only hot recommender
hot_recommender(billboard100)

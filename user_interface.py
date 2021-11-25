# Importing

import pandas as pd
import numpy as np
import hot_recommender as hr
from billboard100_scrapper import billboard100_scrapper

# Loading the songs data

try:

    billboard100 = pd.read_csv(filepath_or_buffer="Data/billboard100.csv")

except FileNotFoundError:

    billboard100 = billboard100_scrapper()


# First Prototype, only hot recommender
hr.hot_recommender_v3(billboard100)

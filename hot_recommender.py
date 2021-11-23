import numpy as np


def hot_recommender(hot_songs):
    
    user_song = input("Please enter one song: ")
    
    if user_song in hot_songs:
        
        recommended_song = np.random.choice(hot_songs)
        
    else:
        
        print("The song you provided us is not popular at the moment. Please try again with a hot song.")
        
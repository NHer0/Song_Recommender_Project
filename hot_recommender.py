import numpy as np


def hot_recommender(songs_data):
    
    songs = np.array(songs_data["song"])
    artists = np.array(songs_data["artist"])
    user_song = input("Please enter the name of one hot song you love: ").lower()
    
    if user_song in songs:
        
        recommended_song = np.random.choice(songs).title()
        index = np.where(songs == recommended_song.lower())
        recommended_artist = artists[index[0][0]].title()
        
        print(f'We think "{recommended_song}" from  "{recommended_artist}" will like you. Check it out!')
        
    else:
        
        print("The song you provided us is not popular at the moment. Please try again with a hot song.")
        
        return
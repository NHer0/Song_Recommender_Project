import numpy as np
import jaro


def hot_recommender_v1(songs_data):
    
    songs = np.array(songs_data["song"])
    artists = np.array(songs_data["artist"])
    user_song = input("Please enter the name of one hot song you love: ").lower()
    
    if user_song in songs:
        
        recommended_song = np.random.choice(songs).title()
        index = np.where(songs == recommended_song.lower())[0]

        if len(index) == 1:

            recommended_artist = artists[index[0]].title()

        else:

            recommended_artist = artists[np.random.choice(index)].title()
        
        print(f'We think "{recommended_song}" from "{recommended_artist}" will like you. Check it out!')

    else:
        
        print("The song you provided us is not popular at the moment. Please try again with a hot song.")
        
    return


def hot_recommender_v2(songs_data):

    match = False

    songs = np.array(songs_data["song"])
    artists = np.array(songs_data["artist"])
    user_song = input("Please enter the name of one hot song you love: ").lower()

    for song in songs:

        jaro_rating = jaro.jaro_winkler_metric(user_song, song)

        if jaro_rating > 0.9:

            user_song = song
            match = True
            break

    if match:

        recommended_song = np.random.choice(songs).title()
        index = np.where(songs == recommended_song.lower())[0]

        if len(index) == 1:

            recommended_artist = artists[index[0]].title()

        else:

            recommended_artist = artists[np.random.choice(index)].title()

        print(f'We think "{recommended_song}" from "{recommended_artist}" will like you. Check it out!')

    else:

        print("The song you provided us is not popular at the moment. Please try again with a hot song.")

    return
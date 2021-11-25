import numpy as np
import jaro
import time


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

    songs = np.array(songs_data["song"])
    artists = np.array(songs_data["artist"])
    match = False
    on = True

    while on:

        match = False
        user_song = input("Please enter the name of one hot song you love: ").lower()

        for song in songs:

            jaro_rating = jaro.jaro_winkler_metric(user_song, song)

            if jaro_rating > 0.92:

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

        print("--------------------------")
        time.sleep(0.5)
        cont = input("Do you want another recommendation? ").lower()

        if cont in ["y", "yes"]:

            print("Awesome! :)")
            print("--------------------------")
            pass

        else:

            print("That's a pity :( See you next time!")
            print("--------------------------")
            on = False

    return


def hot_recommender_v3(songs_data):

    songs = np.array(songs_data["song"])
    artists = np.array(songs_data["artist"])
    match = False
    on = True

    while on:

        match = False
        user_song = input("Please enter the name of one hot song you love: ").lower()
        print("--------------------------")

        for song in songs:

            jaro_rating = jaro.jaro_winkler_metric(user_song, song)

            if jaro_rating > 0.92:

                user_song = song

                if jaro_rating == 1:

                    match = True

                else:

                    answer_typo = input(f'Do you mean "{user_song}"?')
                    print("--------------------------")

                    if answer_typo in ["yes", "y"]:

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
            print("--------------------------")

        else:

            print("The song you provided us is not popular at the moment. Please try again with a hot song.")
            print("--------------------------")

        time.sleep(1)
        cont = input("Do you want another recommendation? ").lower()
        print("--------------------------")

        if cont in ["y", "yes"]:

            print("Awesome! :)")
            print("--------------------------")
            pass

        else:

            print("That's a pity :( See you next time!")
            print("--------------------------")
            on = False

    return

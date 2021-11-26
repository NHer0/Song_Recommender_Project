# Importing Modules

import numpy as np
import jaro
import time
import pandas as pd
import IPython.display
import spotify_api as sp_api
#


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

            if jaro_rating > 0.9:

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


def song_recommender(hot_songs_db, songs_db, kmeans_model, scaler):

    columns_names = ['danceability', 'energy', 'key', 'loudness',
                     'mode', 'speechiness', 'acousticness', 'instrumentalness', 'liveness',
                     'valence', 'tempo'
                     ]

    hot_songs = np.array(hot_songs_db["song"])
    hot_artists = np.array(hot_songs_db["artist"])
    match = False
    on = True

    while on:

        audio_f_list = []
        row = []
        match = False
        feat = True

        user_song = input("Please enter the name of one song you love: ").lower()
        print("--------------------------")

        for song in hot_songs:

            jaro_rating = jaro.jaro_winkler_metric(user_song, song)

            if jaro_rating > 0.92:

                user_song = song

                if jaro_rating == 1:

                    match = True

                else:

                    answer_typo = input(f'Do you mean "{user_song}"? ')
                    print("--------------------------")

                    if answer_typo in ["yes", "y"]:

                        match = True

                    else:

                        print("Oh, then you won't probably like our hot song recommendation. Let's try our song features based recommender!")
                        print("--------------------------")
                break

        if match:

            recommended_song = np.random.choice(hot_songs).title()
            recommended_id = sp_api.sp.search(q=recommended_song, type="track", limit=1, market="US")["tracks"]["items"][0]["id"]
            index = np.where(hot_songs == recommended_song.lower())[0]

            if len(index) == 1:

                recommended_artist = hot_artists[index[0]].title()

            else:

                recommended_artist = hot_artists[np.random.choice(index)].title()

            print(f'You are into hot songs! We think "{recommended_song}" from "{recommended_artist}" will like you. Check it out!')
            print(f'Your song ")
            print("--------------------------")
            player = sp_api.spotify_player(recommended_id)
            IPython.display.display(player)
            print("--------------------------")
            feat_ans = input(f'Are you not satisfied with the hot song recommendation? '
                             f'Do you wanna try our amazing song featured based recommender? ')
            print("--------------------------")

            if feat_ans in ["yes", "y"]:

                match = False

            else:

                pass

        try:

            user_song_id = sp_api.sp.search(q=user_song, type="track", limit=1, market="US")["tracks"]["items"][0]["id"]

        except IndexError:

            odd_ans = input(f'There is something odd! Do you really mean {user_song}? ')
            print("--------------------------")

            if odd_ans in ["yes", "y"]:

                print("You have a weird taste! Your song is not in Spotify Database!")
                print("--------------------------")
                match = True

            else:

                user_song = input("Ops! Please enter again your song: ").lower()
                print("--------------------------")

                user_song_id = sp_api.sp.search(q=user_song, type="track", limit=1, market="US")["tracks"]["items"][0]["id"]

        if not match:

            audio_f = sp_api.sp.audio_features(user_song_id)

            for k in range(11):

                key = list(audio_f[0].keys())[k]
                audio_f_list.append(audio_f[0][key])

            row.append(audio_f_list)
            audio_f_df = pd.DataFrame(row, columns=columns_names)
            X_scaled = scaler.transform(audio_f_df)
            audio_f_scaled_df = pd.DataFrame(X_scaled, columns=columns_names)
            user_song_cluster = kmeans_model.predict(audio_f_scaled_df)
            recommendation = songs_db[songs_db["cluster"] == user_song_cluster[0]].sample()
            recommendation_song = recommendation["song_name"].iloc[0]
            recommendation_artist = recommendation["artist"].iloc[0]
            recommendation_id = recommendation["song_id"].iloc[0]

            print(f'Based on the song features we think "{recommendation_song}" from "{recommendation_artist}" will like you. Check it out!')
            print("--------------------------")
            player = sp_api.spotify_player(recommendation_id)
            IPython.display.display(player)
            print("--------------------------")

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


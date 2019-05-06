import lyricsgenius

genius = lyricsgenius.Genius("client_access_token")

programActive = True

while programActive == True:
    option = input("Would you like to search by artist, or would you like to search specifically for song lyrics? (artist / song) ")

    if option == "artist":
        artist = input("Please type the name of the artist. ")
        type(artist)

        songQuantity = input("How many results would you like?")

        artistSearch = genius.search_artist(artist, max_songs=int(songQuantity), sort="title")
        print(artistSearch.songs)
    elif option == "song":
        artist = input("Please type the name of the artist. ")
        type(artist)
        song = input("Please type the name of the song. ")
        type(song)
        songSearch = genius.search_song(song, artist)
        print("***************************************************")
        print(songSearch.lyrics)
        print("***************************************************")
    else:
        print("Please type 'artist', or 'song' ")

    optionContinue = input("Would you like to continue? (yes / no) ")
    print("***************************************************")
    if optionContinue == "no":
        break






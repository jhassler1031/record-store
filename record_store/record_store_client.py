#API CLI client for record store
import requests

url = "http://localhost:8000/"

#Start Functions

# Login/logout ========================================================================
def login(url):
    username = input("Username: ")
    password = input("Password: ")
    auth_token = requests.post(url + "auth/token/create/", data={"username": username, "password": password}).json()
    auth_token = auth_token["auth_token"]
    return auth_token

def logout(url, user):
    requests.post(url + "auth/token/destroy/", headers={"Authorization": "token " + user})

#Search for something =========================================================
def search(url):
    while True:
        search = input("Enter query or press <enter> to go back: ")
        if search == "":
            return None
        else:
            search_items = requests.get(url + search).json()

        if search_items == []:
            print("No search results found")
        else:
            return search_items

# Display functions for each model to be used in sub menus ====================
def display_band(band):
    print(f"""
Band Name: {band["band_name"]}
ID: {band["id"]}
Genre: {band["genre"]}
City Origin: {band["city_origin"]}
Year Formed: {band["year_formed"]}
""")

def display_album(album):
    print(f"""
ID: {album["id"]}
Title: {album["title"]}
Genre: {album["genre"]}
Release Year: {album["release_year"]}
Notes: {album["notes"]}
Band ID: {album["band"]}
""")

def display_track(track):
    print(f"""
ID: {track["id"]}
Title: {track["title"]}
Album ID: {track["album"]}
    """)


#Sub menu for band options ===================================================
def band_menu(url, user):
    while True:
        print("""
What would you like to do?
1) Show all bands
2) Search for a band
3) Add a band
4) Edit a band
5) Delete a band
Press <enter> to go back
""")
        band_input = input("> ")
        #Show all bands ==========================
        if band_input == "1":
            bands = requests.get(url).json()
            for band in bands:
                display_band(band)
        #Add a band===============================
        elif band_input == "3":
            band_name = input("Band name: ")
            genre = input("Genre: ")
            city_origin = input("City Origin: ")
            year_formed = input("Year formed: ")

            requests.post(url,
            data={"band_name":band_name, "genre": genre, "city_origin": city_origin, "year_formed": year_formed},
            headers={"Authorization": "token " + user})
        #Go back =================================
        elif band_input == "":
            break
        else:
            search_results = search(url + "?band_name=")
            if search_results != None:
                for band in search_results:
                    display_band(band)
                band_id = input("Enter the ID # to select or press <enter> to go back: ")
                if band_id == "":
                    break
                else:
                    band_url = url + band_id
                    band = requests.get(band_url).json()
                if band_input == "2":
                    display_band(band)
                #Update a band =========================
                elif band_input == "4":
                    band_name = input("Band name: ")
                    genre = input("Genre: ")
                    city_origin = input("City Origin: ")
                    year_formed = input("Year formed: ")
                    requests.put(band_url,
                    data={"band_name":band_name, "genre": genre, "city_origin": city_origin, "year_formed": year_formed},
                    headers={"Authorization": "token " + user})
                #Delete a band =========================
                elif band_input == "5":
                    requests.delete(band_url, headers={"Authorization": "token " + user})

# Start of Album Menu =============================================================
def album_menu(url, user):
    while True:
        print("""
What would you like to do?
1) Show all albums
2) Search for an album
3) Add an album
4) Edit an album
5) Delete an album
Press <enter> to go back
""")
        album_input = input("> ")
        #Show all albums ==========================
        if album_input == "1":
            albums = requests.get(url).json()
            for album in albums:
                display_album(album)
        #Add an album ===============================
        elif album_input == "3":
            title = input("Title: ")
            genre = input("Genre: ")
            release_year = input("Release Year: ")
            notes = input("Notes: ")
            band = input("Band ID: ")

            requests.post(url,
            data={"title":title, "genre": genre, "release_year": release_year, "notes": notes, "band": band},
            headers={"Authorization": "token " + user})
        #Go back =================================
        elif album_input == "":
            break
        else:
            search_results = search(url + "?title=")
            if search_results != None:
                for album in search_results:
                    display_album(album)
                album_id = input("Enter the ID # to select or press <enter> to go back: ")
                if album_id == "":
                    break
                else:
                    album_url = url + album_id
                    album = requests.get(album_url).json()
                if album_input == "2":
                    display_album(album)
                #Update an album =========================
                elif album_input == "4":
                    title = input("Title: ")
                    genre = input("Genre: ")
                    release_year = input("Release Year: ")
                    notes = input("Notes: ")
                    band = input("Band ID: ")

                    requests.put(album_url,
                    data={"title":title, "genre": genre, "release_year": release_year, "notes": notes, "band": band},
                    headers={"Authorization": "token " + user})
                #Delete an album =========================
                elif album_input == "5":
                    requests.delete(album_url, headers={"Authorization": "token " + user})

# Start of Track Menu =========================================================
def track_menu(url, user):
    while True:
        print("""
What would you like to do?
1) Show all tracks
2) Search for a track
3) Add a track
4) Edit a track
5) Delete a track
Press <enter> to go back
""")
        track_input = input("> ")
        #Show all tracks ==========================
        if track_input == "1":
            tracks = requests.get(url).json()
            for track in tracks:
                display_track(track)
        #Add a track ===============================
        elif track_input == "3":
            title = input("Title: ")
            album = input("Album ID: ")

            requests.post(url,
            data={"title":title, "album": album},
            headers={"Authorization": "token " + user})
        #Go back =================================
        elif track_input == "":
            break
        else:
            search_results = search(url + "?title=")
            if search_results != None:
                for track in search_results:
                    display_track(track)
                track_id = input("Enter the ID # to select or press <enter> to go back: ")
                if track_id == "":
                    break
                else:
                    track_url = url + track_id
                    track = requests.get(track_url).json()
                if track_input == "2":
                    display_track(track)
                #Update a track =========================
                elif track_input == "4":
                    title = input("Title: ")
                    album = input("Album ID: ")

                    requests.put(track_url,
                    data={"title":title, "album": album},
                    headers={"Authorization": "token " + user})
                #Delete a track =========================
                elif track_input == "5":
                    requests.delete(track_url, headers={"Authorization": "token " + user})


#Start Program
user = login(url)

while True:
    print("""
Choose a section:
1) Bands
2) Albums
3) Tracks
Press <enter> to logout
""")
    main_input = input("> ")
    if main_input == "1":
        band_menu(url + "bands/", user)
    elif main_input == "2":
        album_menu(url + "albums/", user)
    elif main_input == "3":
        track_menu(url + "tracks/", user)
    else:
        logout(url, user)
        break

#API CLI client for record store
import requests

bands_url = "http://localhost:8000/bands/"
albums_url = "http://localhost:8000/albums/"
tracks_url = "http://localhost:8000/tracks/"

#Start Functions

#Search for a band ==============================
def search(url):
    while True:
        search = input("Enter query or press <enter> to go back: ")
        if search == "":
            return None
        else:
            search_item = requests.get(url + search).json()

        if search_item != []:
            return search_item
        else:
            print("No search results found")

#Search sub menu
def get_item_url(url):
    item_id = input("Enter ID of entry to modify or Press <enter> to go back: ")
    if user_input == "":
        break
    else:
        item_url = url + item_id
        return item_url



#Sub menu for band options ======================
def band_menu(url):
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
                print(f"""
Band Name: {band["band_name"]}
ID: {band["id"]}
Genre: {band["genre"]}
City Origin: {band["city_origin"]}
Year Formed: {band["year_formed"]}
""")
        #Add a band===============================
        elif band_input == "3":
            band_name = input("Band name: ")
            genre = input("Genre: ")
            city_origin = input("City Origin: ")
            year_formed = input("Year formed: ")

            request.post(url, data={"band_name":band_name, "genre": genre, "city_origin": city_origin, "year_formed": year_formed})
        #Go back =================================
        elif band_input == "":
            break
        #Ask for the band name to search =========
        else:
            bands = search(url + "?band_name=")
            if bands != None:
            #For just a search, print info =======
                if band_input == "2":
                    for band in bands:
                        print(f"""
ID: {band["id"]}
Band Name: {band["band_name"]}
Genre: {band["genre"]}
City Origin: {band["city_origin"]}
Year Formed: {band["year_formed"]}
""")
                #Update a band =========================
                elif band_input == "4":
                    band.band_name = input("Band name: ")
                    band.genre = input("Genre: ")
                    band.city_origin = input("City Origin: ")
                    band.year_formed = input("Year formed: ")
                    request.put(band_url, data={"band_name":band_name, "genre": genre, "city_origin": city_origin, "year_formed": year_formed})
                #Delete a band =========================
                elif band_input == "5":
                    requests.delete(band_url)


#Start Program
while True:
    print("""
Choose a section:
1) Bands
2) Albums
3) Tracks
Press <enter> to exit
""")
    main_input = input("> ")
    if main_input == "1":
        band_menu(bands_url)
    elif main_input == "2":
        pass
    elif main_input == "3":
        pass
    else:
        break

import configparser
import requests
from bs4 import BeautifulSoup

def getAccessToken():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['Client_Access_Token']['token']

token = getAccessToken()

def searchMusicArtist(artist):
    api_url = "https://api.genius.com/search?q=" + artist
    headers = {"authorization": token}
    r = requests.get(api_url, headers=headers)
    return r.json()

def getArtistID(artist):
    r = searchMusicArtist(artist)
    id = r["response"]["hits"][0]["result"]["primary_artist"]["id"]
    return id

def getTop10Songs(artist):
    id = getArtistID(artist)
    api_url = "https://api.genius.com/artists/" + str(id) + "/songs"
    headers = {"authorization": token}
    params = {
        "sort": "popularity",
        "per_page": 10
    }

    r = requests.get(api_url, headers=headers, params=params)
    return r.json()

def getLyricsList(artist):
    r = getTop10Songs(artist)
    songs = r["response"]["songs"]
    urls = []

    for s in songs:
        urls.append(s["url"])
    
    return urls

def scrapeLyrics(artist):
    links = getLyricsList(artist)
    song_lyrics = []

    for l in links:
        page = requests.get(l)
        soup = BeautifulSoup(page.content, "html.parser")

        try:
            lyrics_div = soup.find(class_="lyrics")

            atags = lyrics_div.find_all("a")
            lyrics = []
        
            for a in atags:
                if len(a.text) > 0 and a.text[0] != "[":
                    lyrics.append(a.text.replace("\n", " NEWLINE "))
            
            song_lyrics.append(lyrics)

        except:
            pass
    
    return song_lyrics
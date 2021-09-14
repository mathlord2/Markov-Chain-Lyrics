from flask import Flask, request, jsonify
from flask_cors import CORS
from lyrics import scrapeLyrics
from markov import MarkovLyrics

app = Flask(__name__)
CORS(app, resources={r'/*' : {'origins': ['http://localhost:3000']}})

def generateArtistLyrics(artist):
    songs = scrapeLyrics(artist)
    m = MarkovLyrics()

    for song in songs:
        m.populateMarkovChain(song)

    return m.generateLyrics().split("NEWLINE")

@app.route("/", methods=["GET", "POST"])
def lyricsGenerator():
    lyrics = []
    if request.method == "POST":
        artist = request.get_json()['data']
        lyrics = generateArtistLyrics(artist)

    return jsonify(result=lyrics)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)
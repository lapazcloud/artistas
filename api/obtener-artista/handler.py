import requests, random, json, os, sys

def handle(req):
    get_random_artist = requests.get("http://ws.audioscrobbler.com/2.0/?method=geo.gettopartists&country=bolivia&api_key=6f065f41e5f2e811666e9c5fe3daa3ec&format=json")

    if get_random_artist.status_code != 200:
        sys.exit("Error when generating a new artist recommendation.")

    random_artist = get_random_artist.json()
    random_artist_index = random.randint(0, len(random_artist["topartists"]["artist"])-1)

    random_artist_name = random_artist["topartists"]["artist"][random_artist_index]["name"]

    get_artist = requests.get("https://api.deezer.com/search/artist?limit=1&q=" + random_artist_name)
    if get_artist.status_code != 200:
        sys.exit("Error when generating a new artist recommendation.")
    artist = get_artist.json()
    artist_id = artist["data"][0]["id"]

    track_url = "https://api.deezer.com/artist/%s/top?limit=3" % (artist_id)
    get_tracks = requests.get(track_url)
    if get_tracks.status_code != 200:
        sys.exit("Error when generating a new artist recommendation.")

    tracks = get_tracks.json()

    response = {}
    response['ranking'] = random_artist_index + 1
    response['name'] = random_artist_name
    response['image'] = artist["data"][0]["picture_xl"]
    response['tracks'] = tracks["data"]

    # Final response
    return json.dumps(response)

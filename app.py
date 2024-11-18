import os
import json
import spotipy
import spotipy.util as util
import requests
from flask import Flask, render_template, request

app = Flask(__name__)


def load_spotify_credentials():
    with open("spotify.json", "r") as keys:
        return json.load(keys)


def load_imagga_credentials():
    with open("Imagga_key.json", "r") as keys:
        return json.load(keys)

@app.route('/', methods=['GET', 'POST'])
def index():
    playlist_info = None
    image_url = None
    error_message = None

    if request.method == 'POST':
        image_url = request.form.get('image_url')  
        
        if not image_url:
            error_message = "Please provide a valid image URL."
            return render_template('index.html', error_message=error_message, playlist_info=None, image_url=None)

        
        try:
            response = requests.get(image_url)
            if response.status_code != 200:
                error_message = "The image URL provided is not valid or accessible."
                return render_template('index.html', error_message=error_message, playlist_info=None, image_url=None)
        except requests.exceptions.RequestException as e:
            error_message = f"Error fetching image: {e}"
            return render_template('index.html', error_message=error_message, playlist_info=None, image_url=None)

        
        api_tokens = load_imagga_credentials()
        api_key = api_tokens["api_key"]
        api_secret = api_tokens["api_secret"]
        response = requests.get(
            f'https://api.imagga.com/v2/tags?image_url={image_url}',
            auth=(api_key, api_secret))

        response_data = response.json()
        tags = response_data['result']['tags']
        tag_keys = [tag['tag']['en'] for tag in tags]

        
        api_tokens = load_spotify_credentials()
        client_id = api_tokens["client_id"]
        client_secret = api_tokens["client_secret"]
        redirectURI = api_tokens["redirect"]
        username = api_tokens["username"]
        scope = 'user-read-private user-read-playback-state user-modify-playback-state playlist-modify-public playlist-modify-private user-library-read'

        token = util.prompt_for_user_token(username, scope, client_id=client_id,
                                           client_secret=client_secret,
                                           redirect_uri=redirectURI)

        sp = spotipy.Spotify(auth=token)

        
        selected_tags = tag_keys[:20]
        search_query = " AND ".join(selected_tags)
        search_results = sp.search(q=search_query, type='track', limit=30)
        music_tracks = [item['id'] for item in search_results['tracks']['items']]

        if music_tracks:
            playlist_name = "Image Playlist"
            playlist_description = "Playlist generated from image tags"
            user_id = sp.current_user()['id']

            playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=True, description=playlist_description)
            sp.playlist_add_items(playlist['id'], music_tracks)

            
            playlist_info = {
                'name': playlist['name'],
                'description': playlist['description'],
                'url': playlist['external_urls']['spotify'],
                'embed_url': f"https://open.spotify.com/embed/playlist/{playlist['id']}"
            }
        else:
            error_message = "No tracks found for the selected tags."

    return render_template('index.html', error_message=error_message, playlist_info=playlist_info, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Blueprint, render_template, url_for, request, redirect, flash
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from flask_login import login_required
from Alexs_wedding_gift.decorators import remote_not_allowed
from Alexs_wedding_gift import app

import spotipy
from spotipy.oauth2 import SpotifyOAuth



spControl = Blueprint('spControl', __name__)

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(username=app.config["SP_USERNAME"], scope=app.config["SP_SCOPE"], client_id=app.config["SP_ID"],
                                               client_secret=app.config["SP_SEC"], redirect_uri=app.config["SP_REDIRECT"], cache_path=app.config["SP_CACHE"]))

class searchForm(FlaskForm):
    artist = StringField('Please enter an artist', validators=[DataRequired()])
    submit =SubmitField('Submit')

class Artist():
    def __init__(self, id, name, uri, cover_url, url_bool=True):
        self.id = id
        self.name = name
        self.uri = uri
        self.cover_url = cover_url
        self.url_bool = url_bool

class Album():
    def __init__(self, id, artist, name, uri, cover_url, url_bool=True):
        self.id = id
        self.artist = artist
        self.name = name
        self.uri = uri
        self.tracks = []
        self.cover_url = cover_url
        self.url_bool = url_bool

class Track():
    def __init__(self, name, uri):
        self.name = name
        self.uri = uri

def fetchDetails(id, object, type):
    if type=="artist":
        try:
            temp = Artist(id, object['name'], object['uri'], object['images'][0]['url'])
        except IndexError:
            temp = Artist(id, object['name'], object['uri'], '', False)

    if type == "album":
        try:
            temp = Album(id, object['artists'][0]['name'], object['name'], object['uri'], object['images'][0]['url'])
        except IndexError:
            temp = Album(id, object['artists'][0]['name'], object['name'], object['uri'], '', False)

        for track in sp.album_tracks(temp.uri)['items']:
            temp.tracks.append(Track(track['name'], track['uri']))
    return temp

"""
@spControl.before_request
def checkToken():
    try:
        sp.search("artist:Foals", type="artist")['artists']['items']
    except Exception as e:
        print(e)
        #token = util.prompt_for_user_token(config.username, config.scope, config.clie_id, config.clie_sec, config.redir)
        token = util.prompt_for_user_token(config.username, config.scope, config.clie_id, config.clie_sec, config.redir, cache_path="/var/www/flaskapps/simpleflask/.cache-thelemmon")
        if token:
            sp.set_auth(token)
"""

@spControl.route('/search', methods=['POST', 'GET'])
@login_required
@remote_not_allowed
def search():
    form = searchForm()
    if request.method == 'POST':
        return redirect(url_for('spControl.artistSearch', search=form.artist.data))
    else:
        return render_template("spSearch.html", form=form)

@spControl.route('/search=<search>', methods=['POST', 'GET'])
@login_required
@remote_not_allowed
def artistSearch(search):
    artist_dict = sp.search("artist:"+search, type="artist")['artists']['items']
    if len(artist_dict) == 0:
        flash("No results for %s could be found" %search)
        return redirect(url_for("spControl.search"))
    artist_list = []
    temp = []
    div = 3
    for id, artist in enumerate(artist_dict):
        temp.append(fetchDetails(id, artist, 'artist'))
        if (id+1)%div == 0:
            artist_list.append(temp)
            temp = []
    artist_list.append(temp)
    return render_template("spSearchResults.html", search=search, artist_list=artist_list, divide=int(12/len(artist_list[0])))

@spControl.route('/search/<uri>', methods=['POST', 'GET'])
@login_required
@remote_not_allowed
def artistPage(uri):
    temp = sp.artist(uri)
    artist = fetchDetails(0, temp, 'artist')

    temp = []
    album_list = []

    related = []

    for id, album in enumerate(sp.artist_albums(uri, country=['US', 'UK'])['items']):
        if album['name'] in temp:
            continue
        else:
            temp.append(album['name'])

        album_list.append(fetchDetails(id, album, 'album'))

    for id, rel in enumerate(sp.artist_related_artists(uri)['artists'][:3]):
        related.append(fetchDetails(id, rel, 'artist'))

    return render_template('spArtistPage.html', album_list=album_list,
                           focus= artist, related=related)

@spControl.route('/adding/<uri>', methods=['POST', 'GET'])
@login_required
@remote_not_allowed
def add_song(uri):
    try:
        sp.add_to_queue(uri)
        flash("Your selection has been succesfully added to the queue")
    except Exception as e:
        print(e)
        flash("Your selection could not be added to the queue. Please check that the client is playing before trying again")
    return redirect(url_for('spControl.search'))


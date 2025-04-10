"""Web API."""

from fastapi import FastAPI

from . import db

app = FastAPI()


# Simple API entry points

@app.get("/artists/")
def artists(id: int | None = None):
    """List all artists.

    If id is not None, the list contains only the artist with given id.

    """
    return db.get_artists(id)


@app.get("/albums/")
def albums(id: int | None = None):
    """List all albums.

    If id is not None, the list contains only the album with given id.

    """
    return db.get_albums(id)


@app.get("/tracks/")
def tracks(id: int | None = None):
    """List all tracks.

    If id is not None, the list contains only the tracks with given id.

    """
    return db.get_tracks(id)


@app.get("/playlists/")
def playlists(id: int | None = None):
    """List all playlists.

    If id is not None, the list contains only the playlist with given id.

    """
    return db.get_playlists(id)


@app.get("/invoices/")
def invoices(id: int | None = None):
    """List all invoices.

    If id is not None, the list contains only the invoice with given id.

    """
    return db.get_invoices(id)


@app.get("/customers/")
def customers(id: int | None = None):
    """List all customers.

    If id is not None, the list contains only the customer with given id.

    """
    return db.get_customers(id)


@app.get("/album_tracks/{album_id}")
def album_tracks(album_id: int):
    """
    List all the tracks of an album.

    """
    return db.get_album_tracks(album_id)


@app.get("/playlist_tracks/{playlist_id}")
def playlist_tracks(playlist_id: int):
    """
    List all the tracks of a playlist.

    """
    return db.get_playlist_tracks(playlist_id)


@app.get("/top_artists/")
def top_artists(top: int | None = 10):
    """Total sales ranking of artists.

    Number of artists is limited to the given top number.

    """
    return db.get_top_artists(top)


@app.get("/top_tracks/")
def top_tracks(top: int | None = 10):
    """Total sales ranking of tracks.

    Number of tracks is limited to the given top number.

    """
    return db.get_top_tracks(top)


@app.get("/top_customers/")
def top_customers(top: int | None = 10):
    """Total sales ranking of customers.

    Number of customers is limited to the given top number.

    """
    return db.get_customers(top)


@app.get("/artists/search/")
def search_artists(term: str = ""):

    return db.get_artist_by_name(term)

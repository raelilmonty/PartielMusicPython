"""Database connection and low-level SQL requests."""

import sqlite3
from pathlib import Path


db = Path(__file__).parents[1] / 'database' / 'database.db'


def get_connection():
    """Get connection to database."""
    connection = sqlite3.connect(db, detect_types=sqlite3.PARSE_DECLTYPES)
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('PRAGMA foreign_keys')
    cursor.close()
    return connection


def get_artists(id=None):
    """List all artists.

    If id is not None, the list contains only the artist with given id.

    """
    cursor = get_connection().cursor()
    if id is None:
        rows = cursor.execute('''
            SELECT *
            FROM Artist
        ''').fetchall()
    else:
        rows = cursor.execute('''
            SELECT *
            FROM Artist
            WHERE ArtistId = ?
        ''', (id,)).fetchall()
    cursor.close()
    return rows


def get_albums(id=None):
    """List all albums.

    If id is not None, the list contains only the album with given id.

    """
    cursor = get_connection().cursor()
    if id is None:
        rows = cursor.execute('''
            SELECT *
            FROM Album
        ''').fetchall()
    else:
        rows = cursor.execute('''
            SELECT *
            FROM Album
            WHERE AlbumId = ?
        ''', (id,)).fetchall()
    cursor.close()
    return rows


def get_tracks(id=None):
    """List all tracks.

    If id is not None, the list contains only the tracks with given id.

    """
    cursor = get_connection().cursor()
    if id is None:
        rows = cursor.execute('''
            SELECT *
            FROM Track
        ''').fetchall()
    else:
        rows = cursor.execute('''
            SELECT *
            FROM Track
            WHERE TrackId = ?
        ''', (id,)).fetchall()
    cursor.close()
    return rows


def get_playlists(id=None):
    """List all playlists.

    If id is not None, the list contains only the playlist with given id.

    """
    cursor = get_connection().cursor()
    if id is None:
        rows = cursor.execute('''
            SELECT *
            FROM Playlist
        ''').fetchall()
    else:
        rows = cursor.execute('''
            SELECT *
            FROM Playlist
            WHERE PlaylistId = ?
        ''', (id,)).fetchall()
    cursor.close()
    return rows


def get_invoices(id=None):
    """List all invoices.

    If id is not None, the list contains only the invoice with given id.

    """
    cursor = get_connection().cursor()
    if id is None:
        rows = cursor.execute('''
            SELECT *
            FROM Invoice
        ''').fetchall()
    else:
        rows = cursor.execute('''
            SELECT *
            FROM Invoice
            WHERE InvoiceId = ?
        ''', (id,)).fetchall()
    cursor.close()
    return rows


def get_customers(id=None):
    """List all customers.

    If id is not None, the list contains only the customer with given id.

    """
    cursor = get_connection().cursor()
    if id is None:
        rows = cursor.execute('''
            SELECT *
            FROM Customer
        ''').fetchall()
    else:
        rows = cursor.execute('''
            SELECT *
            FROM Customer
            WHERE CustomerId = ?
        ''', (id,)).fetchall()
    cursor.close()
    return rows


def get_album_tracks(album_id):
    """
    List all the tracks of an album.

    """
    cursor = get_connection().cursor()
    rows = cursor.execute('''
        SELECT *
        FROM Track
        WHERE AlbumId = ?
    ''', (album_id,)).fetchall()
    cursor.close()
    return rows


def get_playlist_tracks(playlist_id):
    """
    List all the tracks of a playlist.

    """
    cursor = get_connection().cursor()
    rows = cursor.execute('''
        SELECT Playlist.Name, Track.Name, Album.Title
        FROM Playlist
        JOIN PlaylistTrack USING (PlaylistId)
        JOIN Track USING (TrackId)
        JOIN Album USING (AlbumId)
        WHERE PlaylistId = ?
    ''', (playlist_id,)).fetchall()
    cursor.close()
    return rows


def get_top_artists(top=10):
    """Total sales ranking of artists.

    Number of artists is limited to the given top number.

    """
    cursor = get_connection().cursor()
    rows = cursor.execute('''
        SELECT Artist.Name, COUNT(InvoiceLineId) as invoicelines, SUM(InvoiceLine.UnitPrice * Quantity) as total
        FROM Artist
        JOIN Album USING (ArtistId)
        JOIN Track USING (AlbumId)
        JOIN InvoiceLine USING (TrackId)
        GROUP BY Artist.ArtistId
        ORDER BY total DESC
        LIMIT ?
    ''', (top,)).fetchall()
    cursor.close()
    return rows


def get_top_tracks(top=10):
    """Total sales ranking of tracks.

    Number of tracks is limited to the given top number.

    """
    cursor = get_connection().cursor()
    rows = cursor.execute('''
        SELECT Track.Name, SUM(Quantity) as total
        FROM Track
        JOIN InvoiceLine USING (TrackId)
        GROUP BY Track.TrackId
        ORDER BY total DESC
        LIMIT ?
    ''', (top,)).fetchall()
    cursor.close()
    return rows


def get_top_customers(top=10):
    """Total sales ranking of customers.

    Number of customers is limited to the given top number.

    """
    cursor = get_connection().cursor()
    rows = cursor.execute('''
        SELECT CONCAT(FirstName, " ", LastName) as name, SUM(UnitPrice * Quantity) as total
        FROM Customer
        JOIN Invoice USING (CustomerId)
        JOIN InvoiceLine USING (InvoiceId)
        GROUP BY Customer.CustomerId
        ORDER BY total DESC
    ''').fetchall()
    cursor.close()
    return rows

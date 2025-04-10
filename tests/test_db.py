from musics import db, api, cli


def test_artists():
    rows = db.get_artists()
    assert len(rows) > 270


def test_get_artists():
    rows = db.get_artists()
    assert len(rows) > 0
    assert all("ArtistId" in row.keys() and "Name" in row.keys() for row in rows)

    artist = db.get_artists(rows[0]["ArtistId"])
    assert len(artist) == 1


def test_get_albums():
    rows = db.get_albums()
    assert len(rows) > 0
    assert all("AlbumId" in row.keys() and "Title" in row.keys() for row in rows)

    album = db.get_albums(rows[0]["AlbumId"])
    assert len(album) == 1


def test_get_tracks():
    rows = db.get_tracks()
    assert len(rows) > 0
    assert all("TrackId" in row.keys() and "Name" in row.keys() for row in rows)

    track = db.get_tracks(rows[0]["TrackId"])
    assert len(track) == 1


def test_get_playlists():
    rows = db.get_playlists()
    assert len(rows) > 0

    playlist = db.get_playlists(rows[0]["PlaylistId"])
    assert len(playlist) == 1


def test_get_invoices():
    rows = db.get_invoices()
    assert len(rows) > 0

    invoice = db.get_invoices(rows[0]["InvoiceId"])
    assert len(invoice) == 1


def test_get_customers():
    rows = db.get_customers()
    assert len(rows) > 0

    customer = db.get_customers(rows[0]["CustomerId"])
    assert len(customer) == 1


def test_get_album_tracks():
    albums = db.get_albums()
    rows = db.get_album_tracks(albums[0]["AlbumId"])
    assert isinstance(rows, list)


def test_get_playlist_tracks():
    playlists = db.get_playlists()
    rows = db.get_playlist_tracks(playlists[0]["PlaylistId"])
    assert isinstance(rows, list)


def test_get_top_artists():
    rows = db.get_top_artists(5)
    assert len(rows) == 5
    assert all("Name" in row.keys() and "total" in row.keys() for row in rows)


def test_get_top_tracks():
    rows = db.get_top_tracks(5)
    assert len(rows) == 5
    assert all("Name" in row.keys() and "total" in row.keys() for row in rows)


def test_get_top_customers():
    rows = db.get_top_customers(5)
    assert len(rows) == 5
    assert all("Name" in row.keys() and "total" in row.keys() for row in rows)


def test_get_artist_by_name():
    resultats = db.get_artist_by_name("of")
    noms = [artiste["Name"] for artiste in resultats]
    assert any("System Of A Down" in nom for nom in noms)
    assert any("The Office" in nom for nom in noms)


def test_api_search_artist_by_name():
    result = api.search_artists(term="of")
    assert len(result) > 0
    assert any("of" in artist["Name"].lower() for artist in result)


def test_cli_search_artists():
    result = cli.search_artists("of")
    assert "System Of A Down" in result
    assert "The Office" in result
from musics import db


def test_artists():
    rows = db.get_artists()
    assert len(rows) > 270

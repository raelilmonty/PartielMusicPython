from io import StringIO

from musics import cli


def test_top_artists():
    string = StringIO()
    cli.top_artists(file=string)
    text = string.getvalue()
    assert 'Top' in text

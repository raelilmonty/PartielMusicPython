from fastapi.testclient import TestClient

from musics import api


client = TestClient(api.app)


def test_artists():
    response = client.get('/artists/')
    assert response.status_code == 200
    assert len(response.json()) > 100

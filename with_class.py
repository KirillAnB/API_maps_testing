import requests
import pytest


base_url = "https://api.chucknorris.io/jokes/random"
fields = ['id', 'value', 'icon_url', 'url', 'categories']

@pytest.fixture
def get_joke():
    data = requests.get(base_url)
    yield data


class Test_jokes():
    def test_status_code(self, get_joke):
        assert get_joke.status_code == 200

    def test_fields(self, get_joke):
        for field in fields:
            assert field in get_joke.json()

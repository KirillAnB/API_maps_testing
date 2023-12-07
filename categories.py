import pytest
import requests

base_url = "https://api.chucknorris.io/jokes/random"

def test_categories(get_category):
    cat_url = f"{base_url}?category={get_category}"
    response = requests.get(cat_url)

    assert  response.status_code == 200 and get_category in response.json()['categories']

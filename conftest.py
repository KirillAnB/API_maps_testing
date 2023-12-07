import pytest
import requests


@pytest.fixture(params=["animal","career","celebrity","dev","explicit","fashion","food","history","money","movie",
                        "music","political","religion","science","sport","travel"])
def get_category(request):
    category = request.param
    return category

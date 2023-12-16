import pytest
import requests


base_url = "https://rahulshettyacademy.com"  #base url
auth_key = "?key=qaclick123"                 #key for methods


@pytest.fixture
def create_place():
    post_resource = "/maps/api/place/add/json"
    # get_part = "/maps/api/place/get/json"
    post_url = base_url + post_resource + auth_key
    new_place_json_data = {
            "location":{
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy":50,
            "name":"Ocean life resort",
            "phone_number":"(+91) 983 893 3937",
            "address":"29, side layout, cohen 09",
            "types":[
                "hotel",
                "pool place"
            ],
            "website":"www.pussy.com",
            "language":"French-FN"
        }
    result = requests.post(url=post_url, json=new_place_json_data)
    yield result

@pytest.fixture(params = ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website',
                          'language'])
def send_field(request):
    """Sending field to check in the get response"""
    return request.param

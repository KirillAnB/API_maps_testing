import pytest
import requests


json_body_data = {
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



def test_status_code(create_place):
    assert create_place.status_code == 200

def test_creation_status(create_place):
    assert create_place.json().get("status") == 'OK'


def test_if_created(create_place):
    base_url = "https://rahulshettyacademy.com"
    get_url_part = "/maps/api/place/get/json"
    key = "?key=qaclick123"
    place_id = create_place.json().get("place_id")
    full_get_url = base_url + get_url_part + key + '&' + "place_id=" + place_id
    get_result = requests.get(full_get_url)
    for k in get_result.json():
        assert k in json_body_data

def test_put_method(create_place):
    base_url = "https://rahulshettyacademy.com"
    put_url_part = "/maps/api/place/update/json"
    key = "?key=qaclick123"
    full_put_url = base_url + put_url_part + key
    # print(full_put_url)
    place_id = create_place.json().get('place_id')
    # print(place_id)
    put_data = {
        "place_id": place_id,
        "address": "Lenina street 69",
        'key': "qaclick123"
    }
    put_result = requests.put(url=full_put_url, json = put_data)
    assert put_result.json().get("msg") == "Address successfully updated"


@pytest.mark.bad_id
def test_put_method_bad_id(create_place):
    """Testing bad place id answer"""
    base_url = "https://rahulshettyacademy.com"
    put_url_part = "/maps/api/place/update/json"
    key = "?key=qaclick123"
    full_put_url = base_url + put_url_part + key
    # print(full_put_url)
    place_id = create_place.json().get('place_id')
    # print(place_id)
    put_data = {
        "place_id": "bad id",
        "address": "Lenina street 69",
        'key': "qaclick123"
    }
    put_result = requests.put(url=full_put_url, json = put_data)
    assert put_result.json().get("msg") == "Update address operation failed, looks like the data doesn't exists"


def test_delete_method(create_place):
    """Delete plac by place id"""
    base_url = "https://rahulshettyacademy.com"
    delete_url = "/maps/api/place/delete/json"
    key = "?key=qaclick123"
    place_id = create_place.json().get("place_id")
    data_to_delete = {
        "place_id":place_id
    }
    result = requests.delete(url = base_url + delete_url + key, json=data_to_delete)
    assert result.status_code == 200 and result.json().get("status") == "OK"
@pytest.mark.bad_id
def test_bad_id_delete(create_place):
    """Delete plac by place id"""
    base_url = "https://rahulshettyacademy.com"
    delete_url = "/maps/api/place/delete/json"
    key = "?key=qaclick123"
    place_id = create_place.json().get("place_id")
    data_to_delete = {
        "place_id": "bad id"
    }
    result = requests.delete(url = base_url + delete_url + key, json=data_to_delete)
    assert result.status_code == 404 and result.json().get("msg") == """Delete operation failed, looks like the data doesn't exists"""


def test_get_responce(create_place, send_field):
    base_url = "https://rahulshettyacademy.com"
    get_url_part = "/maps/api/place/get/json"
    key = "?key=qaclick123"
    place_id = create_place.json().get("place_id")
    full_get_url = base_url + get_url_part + key + '&' + "place_id=" + place_id
    get_result = requests.get(full_get_url)
    assert send_field in get_result.json()


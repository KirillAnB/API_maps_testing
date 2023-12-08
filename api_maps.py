import requests


base_url = "https://rahulshettyacademy.com"  #base url
auth_key = "?key=qaclick123"                 #key for methods

class Pest_new_location():
    """Maps api testing class"""
    def test_post_new_location(self):
        """New location create"""
        post_resource = "/maps/api/place/add/json"
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
        result = requests.post(url = post_url, json=new_place_json_data)
        new_place_id = result.json()["place_id"]
        print(new_place_id)

if __name__ == '__main__':
    test_method = Pest_new_location()
    test_method.test_post_new_location()


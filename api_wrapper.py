import json
import requests
from pprint import pprint

RESTAURANTS = {each["name"] : each["id"] for each in json.loads(requests.get(
                    "https://d1gvlspmcma3iu.cloudfront.net/restaurants-3d-party.json.gz").content)}

class API:

    def __init__(self, app_id, app_key, user_id=str(0), base_url="https://trackapi.nutritionix.com/"):    #"https://api.nutritionix.com/v1_1"):
        self.app_id = app_id
        self.app_key = app_key
        self.user_id = user_id
        self.base_url = base_url

    def get_food_items(self, restaurant_id):
        return json.loads(requests.get("https://api.nutritionix.com/v1_1/brand",
                     params={"id": restaurant_id,
                             "appId": self.app_id,
                             "appKey": self.app_key}).content)


    def get_food_items_v2(self, restaurant_name):
        return json.loads(requests.get(f"{self.base_url}/v2/search/instant",
                                       headers= {"x-app-id": self.app_id,
                                                 "x-app-key": self.app_key},
                                       params={"query": restaurant_name,
                                               "brand_ids": (RESTAURANTS[restaurant_name])}).content)




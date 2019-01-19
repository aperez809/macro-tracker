import json
import requests

RESTAURANTS = {each["name"] : each["id"] for each in json.loads(requests.get(
                    "https://d1gvlspmcma3iu.cloudfront.net/restaurants-3d-party.json.gz").content)}

class API:

    def __init__(self, app_id, app_key, user_id=0):
        self.app_id = app_id
        self.app_key = app_key
        self.user_id = user_id






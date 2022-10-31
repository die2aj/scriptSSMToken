import requests
import json


response = requests.get("https://api.themoviedb.org/3/authentication/token/new?api_key=725374be1608b260795fe92a785532b0")
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())

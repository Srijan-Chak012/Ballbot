import requests
import json
import random
from datetime import datetime
random.seed(datetime.now())


def GIF(message):
    if len(message) == 4:
        message = "$gif love"
    if message[4] != " ":
        return "Command Not found: Please add a space after $gif"
    url = 'https://api.tenor.com/v1/search?q='+ message[5:] +'&key=SEEQLCR7IAO4&contentfilter=high'
    r = requests.get(url)
    data = r.json()
    results = data["results"]
    index = random.choice(range(0, len(results)))
    return results[index]["url"]


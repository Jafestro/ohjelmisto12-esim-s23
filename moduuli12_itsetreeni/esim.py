import requests
import json

hakusana = input("Anna hakusana: ")


# Pyynnön malli: https://api.tvmaze.com/search/shows?q=girls
pyynto = "https://api.tvmaze.com/search/shows?q=" + hakusana

try:
    vastaus = requests.get(pyynto)

    if vastaus.status_code == 200:
        json_vastaus = vastaus.json()
        print(json.dumps(json_vastaus, indent=2))
        for a in json_vastaus:
            print(a["show"]["name"])
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")

# print(print(json.dumps(vastaus, indent=2)))

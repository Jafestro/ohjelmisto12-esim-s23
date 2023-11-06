import requests

pyynto = "https://api.chucknorris.io/jokes/random"
try:
    vastaus = requests.get(pyynto)
    if vastaus.status_code == 200:
        vastaus_json = vastaus.json()
        vitsi = vastaus_json["value"]
        print(vitsi)
except requests.exceptions.RequestException as e:
    print("Chuck Norris didn't approve that request")

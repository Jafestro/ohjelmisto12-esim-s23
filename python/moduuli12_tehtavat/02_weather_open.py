import requests

api_key = "7ae77191d21c7548e3802d912abbe139"

print("🌡️⛅☀️🌧️🌤️🌦️⛈️☔🌞🌩️🌨️--SÄÄTILA--🌡️⛅☀️🌧️🌤️🌦️⛈️☔🌞🌩️🌨️")

maa = input("Missä maassa oot? >  ")
kaupunki = input("Missä kaupungissa oot? >  ")

pyynto = "https://api.openweathermap.org/data/2.5/weather"

params = {
    'q': f'{kaupunki},{maa}',
    'appid': api_key,
    'units': 'metric'  # jos halumme vastaus celsius-asteina
}

try:
    vastaus = requests.get(pyynto, params=params)
    print(vastaus.url)
    if vastaus.status_code == 200:
        vastaus_json = vastaus.json()
        temprature_in_celsius = vastaus_json['main']['temp']
        saatila = vastaus_json['weather'][0]['main'] + "," + vastaus_json['weather'][0]['description']
        print(f"{kaupunki}, {maa}\n{temprature_in_celsius}°C {saatila}")
    elif vastaus.status_code == 404:
        print("Kaupunki tai maa ei löytyy")
except requests.exceptions.RequestException as e:
    print("Hakua ei voitu suorittaa.")

import mysql.connector
from flask import Flask, Response
import json

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='root',
    autocommit=True
)

kursori = yhteys.cursor()

app = Flask(__name__)


@app.route('/lentokentta/<icao>')
def get_airport_by_icao(icao):
    kursori.execute(f"select name, municipality from airport where ident='{icao}';")
    tulos = kursori.fetchall()
    if tulos:
        name = str(tulos[0][0])
        municipality = str(tulos[0][1])
        status_code = 200

        response = {
            "status": str(status_code),
            "ICAO": str(icao).upper(),
            "Name": str(name),
            "Municipality": str(municipality)
        }

    else:
        status_code = 404
        response = {
            "status": str(status_code),
            "message": "Airport not found"
        }

    json_response = json.dumps(response)
    return Response(response=json_response, status=status_code, mimetype="application/json")


@app.errorhandler(404)
def page_not_found(error):
    response = {
        "status": "404",
        "message": "PAGE_NOT_FOUND"
    }
    json_response = json.dumps(response)
    return Response(response=json_response, status=404, mimetype="application/json")


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

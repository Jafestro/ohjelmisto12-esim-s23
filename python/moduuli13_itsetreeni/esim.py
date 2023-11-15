import json

from flask import Flask, request, render_template, Response

app = Flask(__name__)


@app.route('/summa')
def summa():
    try:
        args = request.args
        num1 = int(args.get("num1"))
        num2 = int(args.get("num2"))
        summa = num1 + num2

        status_code = 200

        vastaus = {
            "status": status_code,
            "num1": num1,
            "num2": num2,
            "summa": summa
        }
    except ValueError:
        status_code = 400
        vastaus = {
            "status": status_code,
            "teksti": "Virheellinen yhteenlaskettava"
        }
        jsonvast = json.dumps(vastaus)
        return Response(response=jsonvast, status=status_code, mimetype="application/json")

    return vastaus


@app.errorhandler(404)
def page_not_found(virhekoodi):
    vastaus = {
        "status": "404",
        "teksti": "Virheellinen päätepiste"
    }
    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")


@app.route('/kaiku/<teksti>')
def kaiku(teksti):
    vastaus = {
        "kaiku": teksti + " " + teksti
    }
    return vastaus


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

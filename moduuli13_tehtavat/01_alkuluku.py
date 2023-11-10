import json

from flask import Flask, Response

app = Flask(__name__)


@app.route('/alkuluku/<number>')
def is_prime_number(number):
    try:
        luku = int(number)
        status_code = 200
        is_prime = False

        if luku <= 1:
            print(f"{luku} ei ole alkuluku")
        else:
            is_prime = True
            for i in range(2, int(luku ** 0.5) + 1):
                if luku % i == 0 and luku != i:
                    is_prime = False
                    break

        response = {
            "status": str(status_code),
            "Number": str(luku),
            "isPrime": str(is_prime)
        }
    except ValueError:
        status_code = 400
        response = {
            "status": str(status_code),
            "message": "BAD_REQUEST"
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

import os
from flask import Flask, request
from requests import get
from flask_cors import CORS, cross_origin

OM2M_ORIGIN = os.getenv('OM2M_ORIGIN')
OM2M_HEADERS = {
    'X-M2M-Origin': OM2M_ORIGIN,
    'Accept': 'application/json'
}

DEV_OM2M_ORIGIN = os.getenv('DEV_OM2M_ORIGIN')
DEV_OM2M_HEADERS = {
    'X-M2M-Origin': DEV_OM2M_ORIGIN,
    'Accept': 'application/json'
}

app = Flask(__name__)
CORS(app)

@app.route("/dev/", defaults={'path': ''})
@app.route("/dev/<path:path>")
@cross_origin()
def proxydev(path):
    args = request.args
    get_param_str = "?"
    for i in args.keys():
        get_param_str += f"{i}={args[i]}&"
    ret = get(url="https://dev-onem2m.iiit.ac.in:443/" + path + get_param_str, headers=DEV_OM2M_HEADERS)
    return ret.json()


@app.route("/", defaults={'path': ''})
@app.route("/<path:path>")
@cross_origin()
def proxy(path):
    args = request.args
    get_param_str = "?"
    for i in args.keys():
        get_param_str += f"{i}={args[i]}&"
    ret = get(url="https://onem2m.iiit.ac.in:443/" + path + get_param_str, headers=OM2M_HEADERS)
    return ret.json()

if __name__ == "__main__":
    app.run("0.0.0.0", 9898)

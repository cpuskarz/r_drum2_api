from flask import Flask, make_response, request, jsonify, Response, url_for
import urllib
import json
import os, sys, socket
import requests
from pymongo import MongoClient

# Phase 3 - p5002


app = Flask(__name__)

#DATASERVER = "http://127.0.0.1:5003"

#client = MongoClient("mongodb://192.168.99.100:27017")



@app.route("/mess", methods=["POST"])
def messit():
    drummer = request.data
    resp = readdrummer(drummer)
    return resp


def readdrummer(drummer):
    s = ""
    with open('drummers/'+ drummer + ".html") as f:
        for l in f:
            l = l.rstrip()
            s += l
    return s


@app.route("/options", methods=["GET"])
def options_route():
    if request.method == "GET":
        page = {"options": option_list()}
        resp = Response(json.dumps(page), content_type='application/json')
        return resp


def option_list():
    options = []
    cur = db.drummers.find()
    for doc in cur:
        if doc['list'] == "drummer_list":
            for index, item in enumerate(doc['names']):
                options.append(item)
    return options



if __name__ == '__main__':
    DATASERVER = os.getenv('mongo_server')
    #client = MongoClient("mongodb://" + DATASERVER)
    client = MongoClient(DATASERVER)
    db = client.primer
    app.run(debug=True, host='0.0.0.0', port=int('5002'))

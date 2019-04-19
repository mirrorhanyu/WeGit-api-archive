from flask import Flask, request
from http import HTTPStatus
import requests

# An instance of this Flask class will be our WSGI application.
app = Flask(__name__)

REPOSITORIES = '/repositories'
DEVELOPERS = '/developers'
LANGUAGES = '/languages'
TRENDING_URL = 'https://github-trending-api.now.sh'

HEADER = {'Content-Type': 'application/json'}

@app.route("/")
def hello():
    return "Hello World!"

@app.route(REPOSITORIES)
def repository():
    params = request.url.split(REPOSITORIES)[1]
    repositories = requests.get(TRENDING_URL + REPOSITORIES + params)
    return repositories.text, HTTPStatus.OK, HEADER

@app.route(DEVELOPERS)
def developer():
    params = request.url.split(DEVELOPERS)[1]
    developers = requests.get(TRENDING_URL + DEVELOPERS + params)
    return developers.text, HTTPStatus.OK, HEADER

@app.route(LANGUAGES)
def language():
    languages = requests.get(TRENDING_URL + LANGUAGES)
    return languages.text, HTTPStatus.OK, HEADER

if __name__ == '__main__':
    app.run()
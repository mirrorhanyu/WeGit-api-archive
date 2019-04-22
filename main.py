from flask import Flask, request
from http import HTTPStatus
import requests
import json

# An instance of this Flask class will be our WSGI application.
app = Flask(__name__)

REPOSITORIES = '/repositories'
DEVELOPERS = '/developers'
LANGUAGES = '/languages'

REPOSITORY = '/repository/<path:path>'

TRENDING_URL = 'https://github-trending-api.now.sh'
GITHUB_API_URL = 'https://api.github.com'
GITHUB_RAW_URL = 'https://raw.githubusercontent.com'

HEADER = {'Content-Type': 'application/json'}
# This key is for temporary use, should be deleted
AUTHORIZATION = {'Authorization': 'Basic bWlycm9yaGFueXU6YjdlNTE0NzAzMWU0YTEyNmM0OTQyMjZhZWRiNzk5Y2EwYTEzMmM1Ng=='}


@app.route("/")
def hello():
    return "Hello World!"


@app.route(REPOSITORIES)
def repository():
    params = request.url.split(REPOSITORIES)[1]
    repositories = requests.get(TRENDING_URL + REPOSITORIES + params).text
    return repositories, HTTPStatus.OK, HEADER


@app.route(DEVELOPERS)
def developer():
    params = request.url.split(DEVELOPERS)[1]
    developers = requests.get(TRENDING_URL + DEVELOPERS + params).text
    return developers, HTTPStatus.OK, HEADER


@app.route(LANGUAGES)
def language():
    languages = requests.get(TRENDING_URL + LANGUAGES).text
    return languages, HTTPStatus.OK, HEADER


@app.route(REPOSITORY)
def repo(path):
    repository = requests.get(GITHUB_API_URL + "/repos/" + path).json()
    readme = requests.get(GITHUB_RAW_URL + "/" + path + "/master/README.md").text
    repository.update({'readme': readme})
    return json.dumps(repository), HTTPStatus.OK, dict(HEADER, **AUTHORIZATION)


if __name__ == '__main__':
    app.run()

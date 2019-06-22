from flask import Flask, request
from http import HTTPStatus
import requests
import json

# An instance of this Flask class will be our WSGI application.
app = Flask(__name__)

REPOSITORIES = '/repositories'
DEVELOPERS = '/developers'
LANGUAGES = '/languages'
USER = '/user'

REPOSITORY = '/repository/<path:path>'
CONTENTS = '/repository/<path:path>/contents'
DEVELOPER = '/developer/<string:name>'
EVENTS = '/users/<string:name>/received_events'
SEARCH = '/search/repositories'

TRENDING_URL = 'https://github-trending-api.now.sh'
GITHUB_API_URL = 'https://api.github.com'
GITHUB_RAW_URL = 'https://raw.githubusercontent.com'

HEADER = {'Content-Type': 'application/json'}
# This key is for temporary use, should be deleted
AUTHORIZATION = {'Authorization': 'Bearer 8046180301de3390aac9c7407e72918a8c5f3b98'}


@app.route('/')
def hello():
    return 'Hello World!'


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
    repository = requests.get(GITHUB_API_URL + '/repos/' + path, headers=AUTHORIZATION).json()
    readme = requests.get(GITHUB_RAW_URL + '/' + path + '/master/README.md').text
    repository.update({'readme': readme})
    return json.dumps(repository), HTTPStatus.OK, HEADER


@app.route(CONTENTS)
def content(path):
    content = requests.get(GITHUB_API_URL + '/repos/' + path + '/contents', headers=AUTHORIZATION).text
    return content, HTTPStatus.OK, HEADER


@app.route(DEVELOPER)
def author(name):
    user = requests.get(GITHUB_API_URL + '/users/' + name, headers=AUTHORIZATION).text
    return user, HTTPStatus.OK, HEADER


@app.route(EVENTS)
def events(name):
    events = requests.get(GITHUB_API_URL + request.full_path, headers=AUTHORIZATION).text
    return events, HTTPStatus.OK, HEADER


@app.route(SEARCH)
def search():
    search = requests.get(GITHUB_API_URL + request.full_path, headers=AUTHORIZATION).text
    return search, HTTPStatus.OK, HEADER


@app.route(USER)
def user():
    user = requests.get(GITHUB_API_URL + USER, headers={'Authorization': request.headers['Authorization']}).text
    return user, HTTPStatus.OK, HEADER


if __name__ == '__main__':
    app.run()

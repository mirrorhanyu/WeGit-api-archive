from flask import Flask, request
import requests

# An instance of this Flask class will be our WSGI application.
app = Flask(__name__)

REPOSITORIES = '/repositories'
DEVELOPERS = '/developers'
LANGUAGES = '/languages'
TRENDING_URL = 'https://github-trending-api.now.sh'

@app.route("/")
def hello():
    return "Hello World!"

@app.route(REPOSITORIES)
def repository():
    params = request.url.split(REPOSITORIES)[1]
    repositories = requests.get(TRENDING_URL + REPOSITORIES + params).json()
    return str(repositories)

@app.route(DEVELOPERS)
def developer():
    params = request.url.split(DEVELOPERS)[1]
    developers = requests.get(TRENDING_URL + DEVELOPERS + params).json()
    return str(developers)

@app.route(LANGUAGES)
def language():
    languages = requests.get(TRENDING_URL + LANGUAGES).json()
    return str(languages)

if __name__ == '__main__':
    app.run()

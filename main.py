import requests
from flask import Flask

from database.database_migration import migrate
from rest.developer import developer_api
from rest.language import language_api
from rest.repository import repository_api
from rest.search import search_api

app = Flask(__name__)


@app.errorhandler(requests.exceptions.RequestException)
def handler_requests_exceptions(error):
    return 'Oops, something went wrong', 500


@app.after_request
def apply_headers_and_status_code(response):
    response.headers['Content-Type'] = 'application/json'
    return response


if __name__ == '__main__':
    migrate()
    app.register_blueprint(developer_api)
    app.register_blueprint(repository_api)
    app.register_blueprint(language_api)
    app.register_blueprint(search_api)
    app.run()

from flask import Flask

import notifications.alter as alter
from rest.developer import developer_api
from rest.language import language_api
from rest.repository import repository_api
from rest.search import search_api

app = Flask(__name__)


@app.errorhandler(Exception)
def handler_requests_exceptions(error):
    alter.to_slack({'text': 'Exception: {}'.format(error.args[0])})
    return 'Oops, something went wrong', 500


@app.after_request
def apply_headers_and_status_code(response):
    response.headers['Content-Type'] = 'application/json'
    return response


if __name__ == '__main__':
    app.register_blueprint(developer_api)
    app.register_blueprint(repository_api)
    app.register_blueprint(language_api)
    app.register_blueprint(search_api)
    app.run()

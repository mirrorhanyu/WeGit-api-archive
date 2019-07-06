import logging

from flask import Flask

import notifications.alter as alter
from rest.developer import developer_api
from rest.health_check import health_check_api
from rest.language import language_api
from rest.repository import repository_api
from rest.search import search_api

app = Flask(__name__)
app.register_blueprint(health_check_api)
app.register_blueprint(developer_api)
app.register_blueprint(repository_api)
app.register_blueprint(language_api)
app.register_blueprint(search_api)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)-15s %(name)-8s %(levelname)-8s %(message)s')
requests_logging = logging.getLogger("urllib3")
requests_logging.setLevel(logging.CRITICAL)
requests_logging.propagate = False


@app.errorhandler(Exception)
def handler_requests_exceptions(error):
    alter.to_slack({'text': 'Exception: {}'.format(error)})
    return 'Oops, something went wrong', 500


@app.after_request
def apply_headers_and_status_code(response):
    response.headers['Content-Type'] = 'application/json'
    return response


if __name__ == '__main__':
    app.run()

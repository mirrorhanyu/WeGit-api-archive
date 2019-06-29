from flask import request, Blueprint
from database_initializer import DatabaseInitializer
from models.account import Account
from settings import settings
import datebase_engine as db
import requests

developer_api = Blueprint('developer', __name__)


@developer_api.route('/trending-developers')
def fetch_trending_developers():
    params = request.url.split(request.url_rule.rule)[1]
    trending_developers = requests.get('{}/{}/{}'.format(settings.GITHUB_TRENDING_HOST, 'developers', params))
    trending_developers.raise_for_status()
    return trending_developers.text


@developer_api.route('/developers')
def fetch_developer():
    name = request.args.get('name')
    token = request.args.get('token')
    if name:
        return _fetch_developer_by_name(name)
    if token:
        return _fetch_developer_by_token(token)


@developer_api.route('/developers/<string:name>/events')
def fetch_developer_events(name):
    token = _get_token()
    events = requests.get('{}/{}/{}/received_events'.format(settings.GITHUB_API_URL, 'users', name),
                          headers={'Authorization': 'token {}'.format(token)})
    events.raise_for_status()
    return events.text


def _fetch_developer_by_name(name):
    token = _get_token()
    developer = requests.get('{}/{}/{}'.format(settings.GITHUB_API_URL, 'users', name),
                             headers={'Authorization': 'token {}'.format(token)})
    developer.raise_for_status()
    return developer.text


def _fetch_developer_by_token(token):
    developer = requests.get('{}/{}'.format(settings.GITHUB_API_URL, 'user'),
                             headers={'Authorization': 'token {}'.format(token)})
    developer.raise_for_status()
    return developer.text


def _get_token():
    token = request.headers.get('Authorization')
    if token is None:
        engine = db.create_database_engine()
        with DatabaseInitializer(engine) as session:
            account = session.query(Account).first()
            return account.token
    else:
        return token

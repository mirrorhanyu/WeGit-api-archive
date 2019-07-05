import requests
from flask import request, Blueprint

from decorators.require_token import require_token
from settings import settings

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
@require_token
def fetch_developer_events(name, token):
    events = requests.get('{}/{}/{}/received_events'.format(settings.GITHUB_API_URL, 'users', name),
                          headers={'Authorization': 'token {}'.format(token)})
    events.raise_for_status()
    return events.text


@require_token
def _fetch_developer_by_name(name, token):
    developer = requests.get('{}/{}/{}'.format(settings.GITHUB_API_URL, 'users', name),
                             headers={'Authorization': 'token {}'.format(token)})
    developer.raise_for_status()
    return developer.text


def _fetch_developer_by_token(token):
    developer = requests.get('{}/{}'.format(settings.GITHUB_API_URL, 'user'),
                             headers={'Authorization': 'token {}'.format(token)})
    developer.raise_for_status()
    return developer.text

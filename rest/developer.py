from flask import request, Blueprint

from decorators.require_requests_session import require_requests_session
from decorators.require_token import require_token
from settings import settings
from utils.pagination import get_max_page

developer_api = Blueprint('developer', __name__)


@developer_api.route('/trending-developers')
@require_requests_session
def fetch_trending_developers(requests_session):
    since = request.args.get('since')
    language = request.args.get('language')
    params = {
        'since': since,
        'language': language
    }
    trending_developers = requests_session.get(
        url='{}/{}'.format(settings.GITHUB_TRENDING_HOST, 'developers'), params=params
    )
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
@require_requests_session
def fetch_developer_events(name, token, requests_session):
    page = request.args.get('page')
    params = {
        'page': page
    }
    events = requests_session.get(url='{}/{}/{}/received_events'.format(settings.GITHUB_API_URL, 'users', name),
                                  headers={'Authorization': 'token {}'.format(token)},
                                  params=params)
    headers = {'Max-Page': get_max_page(events.headers.get('Link'))}
    return events.text, 200, headers


@require_token
@require_requests_session
def _fetch_developer_by_name(name, token, requests_session):
    developer = requests_session.get('{}/{}/{}'.format(settings.GITHUB_API_URL, 'users', name),
                                     headers={'Authorization': 'token {}'.format(token)})
    return developer.text


@require_requests_session
def _fetch_developer_by_token(token, requests_session):
    developer = requests_session.get('{}/{}'.format(settings.GITHUB_API_URL, 'user'),
                                     headers={'Authorization': 'token {}'.format(token)})
    return developer.text

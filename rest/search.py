import json

from flask import Blueprint, request

from decorators.require_requests_session import require_requests_session
from decorators.require_token import require_token
from settings import settings
from utils.pagination import get_max_page

search_api = Blueprint('search', __name__)


@search_api.route('/search/repositories')
@require_token
@require_requests_session
def search(token, requests_session):
    name = request.args.get('name')
    page = request.args.get('page')
    params = {
        'q': name,
        'page': page
    }
    search_result = requests_session.get(
        url='{}/{}/{}'.format(settings.GITHUB_API_URL, 'search', 'repositories'),
        headers={'Authorization': 'token {}'.format(token)},
        params=params
    )
    repositories = json.dumps(search_result.json().get('items'))
    headers = {'Max-Page': get_max_page(search_result.headers.get('Link'))}
    return repositories, 200, headers

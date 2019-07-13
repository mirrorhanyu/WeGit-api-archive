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
    query_repository = request.args.get('name')
    repositories = requests_session.get(
        url='{}/{}/{}?q={}'.format(settings.GITHUB_API_URL, 'search', 'repositories', query_repository),
        headers={'Authorization': 'token {}'.format(token)})
    headers = {'Max-Page': get_max_page(repositories.headers.get('Link'))}
    return repositories.text, 200, headers

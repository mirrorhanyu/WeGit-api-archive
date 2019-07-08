from flask import Blueprint, request

from decorators.require_requests_session import require_requests_session
from decorators.require_token import require_token
from settings import settings

search_api = Blueprint('search', __name__)


@search_api.route('/search/repositories')
@require_token
@require_requests_session
def search(token, requests_session):
    query_repository = request.args.get('repository')
    repositories = requests_session.get(
        '{}/{}/{}?q={}'.format(settings.GITHUB_API_URL, 'search', 'repositories', query_repository),
        headers={'Authorization': 'token {}'.format(token)})
    return repositories.text

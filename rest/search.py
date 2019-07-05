import requests
from flask import Blueprint, request

from decorators.require_token import require_token
from settings import settings

search_api = Blueprint('search', __name__)


@search_api.route('/search/repositories')
@require_token
def search(token):
    query_repository = request.args.get('repository')
    repositories = requests.get('{}/{}?q={}'.format(settings.GITHUB_API_URL, 'repositories', query_repository),
                                headers={'Authorization': 'token {}'.format(token)})
    repositories.raise_for_status()
    return repositories.text

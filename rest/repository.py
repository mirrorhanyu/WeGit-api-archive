import json

import requests
from flask import request, Blueprint

from decorators.require_token import require_token
from settings import settings

repository_api = Blueprint('repository', __name__)


@repository_api.route('/trending-repositories')
def fetch_trending_repositories():
    params = request.url.split(request.url_rule.rule)[1]
    trending_repositories = requests.get('{}/{}/{}'.format(settings.GITHUB_TRENDING_HOST, 'repositories', params))
    trending_repositories.raise_for_status()
    return trending_repositories.text


@repository_api.route('/repositories')
@require_token
def fetch_repository_by_owner_and_repo_name(token):
    owner = request.args.get('owner')
    name = request.args.get('name')
    repository = requests.get('{}/{}/{}/{}'.format(settings.GITHUB_API_URL, 'repos', owner, name),
                              headers={'Authorization': 'token {}'.format(token)}).json()
    readme = requests.get('{}/{}/{}/master/README.md'.format(settings.GITHUB_RAW_URL, owner, name)).text
    repository.update({'readme': readme})
    return json.dumps(repository)

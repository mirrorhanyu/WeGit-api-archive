import json

from flask import request, Blueprint

from decorators.require_requests_session import require_requests_session
from decorators.require_token import require_token
from settings import settings

repository_api = Blueprint('repository', __name__)


@repository_api.route('/trending-repositories')
@require_requests_session
def fetch_trending_repositories(requests_session):
    params = request.url.split(request.url_rule.rule)[1]
    trending_repositories = requests_session.get(
        '{}/{}/{}'.format(settings.GITHUB_TRENDING_HOST, 'repositories', params))
    return trending_repositories.text


@repository_api.route('/repositories')
@require_token
@require_requests_session
def fetch_repository_by_owner_and_repo_name(token, requests_session):
    owner = request.args.get('owner')
    name = request.args.get('name')
    repository = requests_session.get('{}/{}/{}/{}'.format(settings.GITHUB_API_URL, 'repos', owner, name),
                                      headers={'Authorization': 'token {}'.format(token)}).json()
    readme = requests_session.get('{}/{}/{}/master/README.md'.format(settings.GITHUB_RAW_URL, owner, name)).text
    repository.update({'readme': readme})
    return json.dumps(repository)

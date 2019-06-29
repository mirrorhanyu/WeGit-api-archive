import json

import requests
from flask import request, Blueprint

import database.datebase_engine as db
from database.database_initializer import DatabaseInitializer
from database.models.account import Account
from settings import settings

repository_api = Blueprint('repository', __name__)


@repository_api.route('/trending-repositories')
def fetch_trending_repositories():
    params = request.url.split(request.url_rule.rule)[1]
    trending_repositories = requests.get('{}/{}/{}'.format(settings.GITHUB_TRENDING_HOST, 'repositories', params))
    trending_repositories.raise_for_status()
    return trending_repositories.text


@repository_api.route('/repositories')
def fetch_repository_by_owner_and_repo_name():
    owner = request.args.get('owner')
    name = request.args.get('name')
    token = _get_token(request.headers)
    repository = requests.get('{}/{}/{}/{}'.format(settings.GITHUB_API_URL, 'repos', owner, name),
                              headers={'Authorization': 'token {}'.format(token)}).json()
    readme = requests.get('{}/{}/{}/master/README.md'.format(settings.GITHUB_RAW_URL, owner, name)).text
    repository.update({'readme': readme})
    return json.dumps(repository)


def _get_token(request_headers):
    token = request_headers.get('Authorization')
    if token is None:
        engine = db.create_database_engine()
        with DatabaseInitializer(engine) as session:
            account = session.query(Account).first()
            return account.token
    else:
        return token

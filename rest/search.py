import requests
from flask import Blueprint, request

import database.datebase_engine as db
from database.database_initializer import DatabaseInitializer
from database.models.account import Account
from settings import settings

search_api = Blueprint('search', __name__)


@search_api.route('/search/repositories')
def search():
    token = _get_token()
    query_repository = request.args.get('repository')
    repositories = requests.get('{}/{}?q={}'.format(settings.GITHUB_API_URL, 'repositories', query_repository),
                                headers={'Authorization': 'token {}'.format(token)})
    repositories.raise_for_status()
    return repositories.text


def _get_token():
    token = request.headers.get('Authorization')
    if token is None:
        engine = db.create_database_engine()
        with DatabaseInitializer(engine) as session:
            account = session.query(Account).first()
            return account.token
    else:
        return token

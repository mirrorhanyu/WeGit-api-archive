from flask import Blueprint

from decorators.require_requests_session import require_requests_session
from settings import settings

language_api = Blueprint('language', __name__)


@language_api.route('/trending-languages')
@require_requests_session
def fetch_trending_languages(requests_session):
    trending_languages = requests_session.get('{}/{}'.format(settings.GITHUB_TRENDING_HOST, 'languages'))
    return trending_languages.text

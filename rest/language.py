import requests
from flask import Blueprint

from settings import settings

language_api = Blueprint('language', __name__)


@language_api.route('/trending-languages')
def fetch_trending_languages():
    trending_languages = requests.get('{}/{}'.format(settings.GITHUB_TRENDING_HOST, 'languages'))
    trending_languages.raise_for_status()
    return trending_languages.text

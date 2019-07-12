from flask import Blueprint
import json

language_api = Blueprint('language', __name__)


@language_api.route('/trending-languages')
def fetch_trending_languages():
    popular_languages = json.dumps(['CSS', 'Go', 'HTML', 'Java', 'Javascript', 'Python', 'Typescript'])
    return popular_languages

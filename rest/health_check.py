from flask import Blueprint

health_check_api = Blueprint('health_check_api', __name__)


@health_check_api.route('/health-check')
def health_check():
    return "ok"

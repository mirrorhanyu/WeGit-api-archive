import requests

from settings import settings


def to_slack(message):
    requests.post(url=settings.NOTIFICATION_SLACK_ALERT, json=message)

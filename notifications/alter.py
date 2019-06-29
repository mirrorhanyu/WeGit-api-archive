import requests

from settings import settings


def to_slack(message):
    requests.post(settings.NOTIFICATION_SLACK_ALERT, data=message,
                  headers={'Content-type': 'application/json'})

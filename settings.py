import os


class Settings(object):
    def __init__(self):
        self.DATABASE_USERNAME = os.environ.get('DATABASE_USERNAME')
        self.DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
        self.DATABASE_ENDPOINT = os.environ.get('DATABASE_ENDPOINT')
        self.DATABASE_NAME = os.environ.get('DATABASE_NAME')

        self.GITHUB_TRENDING_HOST = 'https://github-trending-api.now.sh'
        self.GITHUB_API_URL = 'https://api.github.com'
        self.GITHUB_RAW_URL = 'https://raw.githubusercontent.com'

        self.NOTIFICATION_SLACK_ALERT = os.environ.get('NOTIFICATION_SLACK_ALERT')


settings = Settings()

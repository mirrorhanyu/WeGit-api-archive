import os


class Settings(object):
    def __init__(self):
        self.DATABASE_USERNAME = os.environ.get('DATABASE_USERNAME')
        self.DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
        self.DATABASE_ENDPOINT = os.environ.get('DATABASE_ENDPOINT')
        self.DB_NAME = os.environ.get('DB_NAME')

        self.DATABASE_MIGRATION = 'migration'
        self.DATABASE_MIGRATION_NAME = 'gitter-server'

        self.GITHUB_TRENDING_HOST = 'https://github-trending-api.now.sh'
        self.GITHUB_API_URL = 'https://api.github.com'
        self.GITHUB_RAW_URL = 'https://raw.githubusercontent.com'


settings = Settings()

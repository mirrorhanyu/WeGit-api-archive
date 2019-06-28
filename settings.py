import os


class Settings(object):
    def __init__(self):
        self.database_username = os.environ.get("DATABASE_USERNAME")
        self.database_password = os.environ.get("DATABASE_PASSWORD")
        self.database_endpoint = os.environ.get("DATABASE_ENDPOINT")
        self.db_name = os.environ.get("DB_NAME")


settings = Settings()

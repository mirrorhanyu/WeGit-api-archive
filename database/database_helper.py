from settings import settings


def get_database_url():
    username = settings.DATABASE_USERNAME
    password = settings.DATABASE_PASSWORD
    endpoint = settings.DATABASE_ENDPOINT
    database_name = settings.DATABASE_NAME
    return "postgresql://%s:%s@%s/%s" % (username, password, endpoint, database_name)

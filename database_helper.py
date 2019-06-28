from settings import settings


def get_database_url():
    username = settings.DATABASE_USERNAME
    password = settings.DATABASE_PASSWORD
    endpoint = settings.DATABASE_ENDPOINT
    db_name = settings.DB_NAME
    return "postgresql://%s:%s@%s/%s" % (username, password, endpoint, db_name)

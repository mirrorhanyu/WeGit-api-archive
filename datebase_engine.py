from sqlalchemy import create_engine, pool

from settings import settings


class DatabaseEngine:
    instance = None

    @staticmethod
    def fetch():
        if not DatabaseEngine.instance:
            DatabaseEngine.instance = _create_database_engine()
        return DatabaseEngine.instance


def create_database_engine():
    return DatabaseEngine.fetch()


def _create_database_engine():
    engine = create_engine(get_database_url(), echo=False, pool_size=0, connect_args={'sslmode': 'require'},
                           poolclass=pool.QueuePool)
    return engine


def close_database_engine(engine):
    engine.dispose()


def get_database_url():
    username = settings.database_username
    password = settings.database_password
    endpoint = settings.database_endpoint
    db_name = settings.db_name
    return "postgresql://%s:%s@%s/%s" % (username, password, endpoint, db_name)

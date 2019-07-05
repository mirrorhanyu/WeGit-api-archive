import functools

from flask import request

import database.datebase_engine as db
from database.database_initializer import DatabaseInitializer
from database.models.account import Account


def require_token(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if token is None:
            engine = db.create_database_engine()
            with DatabaseInitializer(engine) as session:
                account = session.query(Account).first()
                token = account.token
        return func(*args, **kwargs, token=token)

    return wrapper

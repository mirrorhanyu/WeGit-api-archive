from sqlalchemy import Table, MetaData, Column, Integer, String

meta = MetaData()

account = Table(
    'account', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(40)),
    Column('token', String(40)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    meta.bind = migrate_engine
    account.create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    meta.bind = migrate_engine
    account.drop()

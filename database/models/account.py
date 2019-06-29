from sqlalchemy import Column, Integer, Sequence, String

from database.models.base import Base


class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, Sequence('id'), primary_key=True)
    name = Column(String(40))
    token = Column(String(40))

    def __repr__(self):
        return "<Account(name='%s', token='%s')>" % (self.name, self.token)

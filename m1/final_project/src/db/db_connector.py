import sqlalchemy as database
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.elements import and_, or_
from .models import *
from os import getenv


class Database:
    def __init__(self):
        engine = database.create_engine(getenv("DATABASE"))
        self.session = sessionmaker(bind=engine)

    def get_user(self, tg_id):
        with self.session() as session:
            with session.begin():
                query = session\
                    .query(User)\
                    .filter(User.tg_id.__eq__(tg_id))\
                    .scalar()

                if query:
                    return dict(tg_name=query.tg_name, tg_username=query.tg_username)
                return False

    def save_user(self, tg_id, tg_name, tg_username):
        with self.session() as session:
            with session.begin():
                user = User(
                    tg_id=tg_id,
                    tg_name=tg_name,
                    tg_username=tg_username
                )
                session.add(user)

    def remove_user(self, tg_id):
        with self.session() as session:
            with session.begin():
                session.query(User).filter(User.tg_id.__eq__(tg_id)).delete()

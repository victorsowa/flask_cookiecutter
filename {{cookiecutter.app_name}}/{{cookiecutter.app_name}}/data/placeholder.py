import sqlalchemy
from {{cookiecutter.app_name}}.data.modelbase import SqlAlchemyBase


class Placeholder(SqlAlchemyBase):
    __tablename__ = 'placeholder'

    placeholder_int: int = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    placeholder_str: str = sqlalchemy.Column(sqlalchemy.String, primary_key=True)

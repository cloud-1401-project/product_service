import sqlalchemy
from config import metadata


''' SQLAlchemy Model'''
products = sqlalchemy.Table(
    "products",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String(100), unique=True),
    sqlalchemy.Column("count_in_storage", sqlalchemy.Integer),
)
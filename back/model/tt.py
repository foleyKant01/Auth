import datetime
import uuid
from config.db import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import expression
from sqlalchemy.dialects.mysql import MEDIUMTEXT
from sqlalchemy import Text  # en haut de ton fichier si ce n'est pas déjà fait


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.String(128), unique=True, default=lambda: str(uuid.uuid4()))
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    motpreferer = db.Column(db.String(128), nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)
    update_date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

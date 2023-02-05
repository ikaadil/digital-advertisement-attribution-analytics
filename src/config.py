import os
from flask_sqlalchemy import SQLAlchemy

SECRET_KEY = os.urandom(32)
db = SQLAlchemy()

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI_CONNECTION")

SQLALCHEMY_TRACK_MODIFICATIONS = False

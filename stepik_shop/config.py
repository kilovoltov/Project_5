import os


class Config:
    DEBUG = True
    SECRET_KEY = b'_5#y2L"gpHF4Q8z]/IPHYv2nmbN|cu{?ysw3GY1He2X'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

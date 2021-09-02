import os


class Config(object):
    SECRET_KEY = 'MY_SECRET_KEY'


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:@localhost/cinecalidad'


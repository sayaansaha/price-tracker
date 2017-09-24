import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
  DEBUG = False
  TESTING = False
  CSRF_ENABLED = True
  api_key = 'AIzaSyCcPSWB7n1aj2hx4TCM_aJDBW2QHhLqQSA'
  SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
  DEBUG = False


class StagingConfig(Config):
  DEVELOPMENT = True
  DEBUG = True


class DevelopmentConfig(Config):
  DEVELOPMENT = True
  DEBUG = True


class TestingConfig(Config):
  TESTING = True

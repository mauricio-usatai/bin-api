import os

class Config():
  VERSION = os.environ.get('VERSION', None)
  SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-env-key')
  REDIS_URL = os.environ.get('REDIS_URL', 'localhost')
  REDIS_PORT = int(os.environ.get('REDIS_PORT', '6379'))
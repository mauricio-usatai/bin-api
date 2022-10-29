import app as App

def check_auth_key(key):
  return key == App.Config.SECRET_KEY
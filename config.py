# import os
# basedir = os.path.abspath(os.path.dirname(__file__)) # this is an absolute path for where the config.py exist

# class Config(object):
# # ...
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
#     'sqlite:///' + os.path.join(basedir, 'app.db') # This is a fallback value
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'amelSecrectKey'

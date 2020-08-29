import os

basedir = "\\".join(os.path.abspath(os.path.dirname(__file__)).split("\\")[:-2])

class Config():
    SECRET_KEY = os.getenv("SECRET_KEY")
    BASE_DIR = basedir
    SP_USERNAME = os.getenv("SP_USERNAME")
    SP_SCOPE = os.getenv("SP_SCOPE")
    SP_ID = os.getenv("SP_ID")
    SP_SEC = os.getenv("SP_SEC")
    SP_REDIRECT = os.getenv("SP_REDIRECT")
    SP_CACHE = os.getenv("SP_CACHE")
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:22:43 2020

@author: thele


"""
import sys

print(sys.executable)

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from .views.config import Config
#from .views.testConfig import TestConfig

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
#app.config.from_object(TestConfig)
app.config.from_object(Config)

bootstrap = Bootstrap(app)

db = SQLAlchemy(app)
login = LoginManager(app)

from . import flaskr
from .views import SpControl
from .views import app_auth
from .views import app_messages

app.register_blueprint(SpControl.spControl)
app.register_blueprint(app_auth.auth)
app.register_blueprint(app_messages.app_message)

login.login_view = "auth.login"



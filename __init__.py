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
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.secret_key = os.urandom(16)
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from . import flaskr
from .views import SpControl
from .views import app_auth

app.register_blueprint(SpControl.spControl)
app.register_blueprint(app_auth.auth)



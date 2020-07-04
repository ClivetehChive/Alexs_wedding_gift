# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:22:43 2020

@author: thele


"""
import sys

print(sys.executable)

from flask import Flask
app = Flask(__name__)
from . import flaskr

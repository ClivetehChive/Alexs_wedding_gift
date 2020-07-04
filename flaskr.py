import numpy
from Alexs_wedding_gift import app
from flask import Flask, redirect, url_for
from .views import SpControl as spControl
from flask_bootstrap import Bootstrap

app.secret_key = "tempKey"
app.register_blueprint(spControl.spControl)
bootstrap = Bootstrap(app)

@app.route('/')
def home():
    return redirect(url_for('spControl.search'))

if __name__ == '__main__':
    app.run()

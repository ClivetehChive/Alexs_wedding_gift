import numpy
<<<<<<< HEAD
from flask import Flask, redirect, url_for
from .views.placeholder import example_blueprint
from . import app
=======
from Alexs_wedding_gift import app
from flask import Flask, redirect, url_for
import views.SpControl as spControl
from flask_bootstrap import Bootstrap
>>>>>>> 2327c9f7eda434e6a14a59357316f31f9ba264c4

app.secret_key = "tempKey"
app.register_blueprint(spControl.spControl)
bootstrap = Bootstrap(app)

@app.route('/')
def home():
    return redirect(url_for('spControl.search'))

if __name__ == '__main__':
    app.run()

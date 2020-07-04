import numpy
from flask import Flask, redirect, url_for
import views.SpControl as spControl
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "tempKey"
app.register_blueprint(spControl.spControl)
bootstrap = Bootstrap(app)

@app.route('/')
def home():
    return redirect(url_for('spControl.search'))

if __name__ == '__main__':
    app.run(host="192.168.0.177", debug=True)
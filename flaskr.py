import numpy
from flask import Flask, redirect, url_for
from views.placeholder import example_blueprint

app = Flask(__name__)
app.register_blueprint(example_blueprint)

@app.route('/')
def home():
    return redirect(url_for('example.test'))

if __name__ == '__main__':
    app.run()
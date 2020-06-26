import numpy
from flask import Flask, redirect, url_for
from views.placeholder import example_blueprint
from Alexs_wedding_gift import app

app.register_blueprint(example_blueprint)

@app.route('/')
def home():
    return redirect(url_for('example.test', variable='This is the passed variable'))

if __name__ == '__main__':
    app.run()
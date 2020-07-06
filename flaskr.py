import numpy
if __name__ != "__main__":
    from Alexs_wedding_gift import app
from flask import Flask, redirect, url_for, render_template, request, session
import views.SpControl as spControl
from flask_bootstrap import Bootstrap
import os

from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
import sys

if __name__ == "__main__":
    app = Flask(__name__)

app.secret_key = os.urandom(16)
app.register_blueprint(spControl.spControl)
bootstrap = Bootstrap(app)

class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField('Submit')

class Image():
    def __init__(self, id, path):
        self.id=id
        self.path=path

@app.route('/', methods=['POST', 'GET'])
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    form = LoginForm()
    print("This is working")
    return render_template("app_login.html", form=form)

@app.route('/login', methods=['POST', 'GET'])
def login_post_get():
    form = LoginForm()
    print(form.password, file=sys.stdout)
    if form.validate_on_submit():
        if form.password.data=="Meeseeks":
            return redirect(url_for('home'))

    return redirect(url_for('login'))

@app.route('/home')
def home():
    image_list = [Image(no, path) for no, path in enumerate(os.listdir(app.root_path+"/static/images/"))]
    return render_template("app_home.html", image_list=image_list)

@app.route('/messages')
def messages():
    return "This is the message submition page"

@app.route('/schedule')
def schedule():
    return "This is the schedule page"

if __name__ == '__main__':
    app.run(host="192.168.0.177", debug=True)
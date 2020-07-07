from flask import Blueprint, render_template, url_for, redirect, flash
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from Alexs_wedding_gift.models import User, Post
from werkzeug.security import check_password_hash
import sys


auth = Blueprint('auth', __name__)

class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField('Submit')

@auth.route('/login')
def login():
    form = LoginForm()
    return render_template("app_login.html", form=form)

@auth.route('/login', methods=['POST', 'GET'])
def login_post_get():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None:
            if check_password_hash(user.password_hash, form.password.data):
                print("welcome ", user.username)
                print(Post.query.all()[0].user.role.name)
                return redirect(url_for('home'))
            flash("Your username or password is incorrect please try again")

    return redirect(url_for('index'))
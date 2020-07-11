from flask import Blueprint, render_template, url_for, redirect, flash, request
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from Alexs_wedding_gift.models import User
from flask_login import current_user, login_user

auth = Blueprint('auth', __name__)

class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    submit = SubmitField('Submit')

@auth.route('/login', methods=['POST', 'GET'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            if next_page == '/' or next_page is None:

                next_page = url_for('index')
            return redirect(next_page)
        flash("Your username or password is incorrect please try again")

    return render_template("app_login.html", form=form)
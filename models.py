from . import db
from . import login
from werkzeug.security import check_password_hash
from flask_login import UserMixin


class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(10), unique=True)
    user = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' %self.name

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(20), unique=True)
    password_hash = db.Column(db.String(120))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    post = db.relationship('Post', backref='user')

    def __repr__(self):
        return '<User %r>' %self.username

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def can(self, role):
        return self.role is not None and self.role.name == role

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True, unique=True)
    timestamp = db.Column(db.DateTime)
    file_url = db.Column(db.String(120), default='')
    message = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return '<Post %r>' %self.timestamp

@login.user_loader
def load_uder(id):
    return User.query.get(int(id))
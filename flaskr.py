from Alexs_wedding_gift import app
from flask import redirect, url_for, render_template
from flask_login import login_required
from .decorators import admin_required
from .models import Post
from sqlalchemy import desc
import os

class Image():
    def __init__(self, id, path):
        self.id=id
        self.path=path

@app.route('/', methods=['POST', 'GET'])
def index():
    return redirect(url_for('auth.login'))

@app.route('/home')
@login_required
def home():
    posts = Post.query.order_by(desc(Post.timestamp)).limit(10).all()
    image_list = [Image(no, path) for no, path in enumerate(os.listdir(app.root_path+"/static/images/"))]
    return render_template("app_home.html", image_list=image_list, posts=posts)

@app.route('/schedule', methods=['POST', 'GET'])
@login_required
def schedule():
    return "This is a placeholder for a schedule page"

@app.route('/root', methods=['POST', 'GET'])
@login_required
@admin_required
def root():
    return "This is a placeholder for a engineering panel"

if __name__ == '__main__':
    app.run(host="192.168.0.177", debug=True)
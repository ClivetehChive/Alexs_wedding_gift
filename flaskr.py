from Alexs_wedding_gift import app
from flask import redirect, url_for, render_template
import os

class Image():
    def __init__(self, id, path):
        self.id=id
        self.path=path

@app.route('/', methods=['POST', 'GET'])
def index():
    return redirect(url_for('auth.login'))

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
from flask import Blueprint, render_template, url_for, redirect, flash
from wtforms import SubmitField, TextAreaField, FileField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from Alexs_wedding_gift.models import Post
from Alexs_wedding_gift import db, basedir
from flask_login import current_user, login_required
from datetime import datetime
from sqlalchemy import desc

app_message = Blueprint('app_message', __name__)

class MessageForm(FlaskForm):
    message = TextAreaField(label="Message:", validators=[DataRequired()])
    file = FileField(label="Please attach a photo")
    submit = SubmitField("Submit")

@app_message.route("/post_message", methods=["GET"])
@login_required
def messages():
    form = MessageForm()
    posts = Post.query.order_by(desc(Post.timestamp)).limit(20).all()
    return render_template("app_messages.html", form=form, posts=posts)

@app_message.route('/post_message', methods=["POST"])
@login_required
def messages_post():
    form = MessageForm()
    if form.validate_on_submit():
        timestamp = datetime.now()
        print(form.file.data.filename)

        if form.file.data.filename != "":
            file_timestamp = str(timestamp.date())+"-"+str(timestamp.time().hour)+"-"+str(timestamp.time().minute)+"-"+str(timestamp.time().second)
            file_loc ="user_submitted/"+str(current_user.id)+"-"+file_timestamp+".jpeg"
            form.file.data.save(basedir+"/static/"+file_loc)
            file_loc = url_for("static", filename=file_loc)
        else:
            file_loc = ""
        post = Post(timestamp=timestamp, message=form.message.data, user=current_user, file_url=file_loc)
        db.session.add(post)
        db.session.commit()
        print(file_loc, post.file_url)
        flash("Thank you for leaving a message/image for Dom and Kim")

    return redirect(url_for("app_message.messages"))
from flask import Flask, render_template, request, jsonify, escape
from app import app, models, db

import sendgrid
from sendgrid.helpers.mail import *
import os

sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))




@app.route('/')
@app.route('/index')
def index():

    posts = models.Post.query.order_by(models.Post.id.desc()).limit(20)
    return render_template('index.html',posts=posts)

@app.route('/posts',methods=['POST'])
def posts():

    try:
        title = request.form.get('title') or ""
        body = request.form.get('body')
        p = models.Post(body=body, title=title)
        db.session.add(p)
        db.session.commit()
    except:
        print("############Error with database")


    try:
        from_email = Email("theUsStory@samkreter.com")
        subject = "New Post: " + title
        to_email = Email("samkreter@gmail.com")
        content = Content("text/plain", body)
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
        print("response: ",response.status_code)
        print("body: ", response.body)
        print("headers: ",response.headers)
    except:
        print("###################### Failed to send email")


    return jsonify(
        {
            'error':1,
            'title':escape(title),
            'body':escape(body)

        })

from flask import Flask, render_template, request, jsonify
from app import app, models, db

@app.route('/')
@app.route('/index')
def index():

    posts = models.Post.query.all()
    return render_template('index.html',posts=posts)

@app.route('/posts',methods=['GET'])
def posts():
    title = request.args.get('title')
    body = request.args.get('body')
    p = models.Post(body=body, title=title)
    db.session.add(p)
    db.session.commit()
    return jsonify(
        {
            'error':1,
            'title':title,
            'body':body

        })

from flask import Flask, render_template, request, jsonify
from app import app, models

@app.route('/')
@app.route('/index')
def index():

    posts = models.Post.query.all()
    return render_template('index.html',posts=posts)
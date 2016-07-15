# -*- coding: utf-8 -*-
from website import app
from flask import render_template

@app.context_processor
def config_template():
    return dict(template = "layout.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/education")
def education():
    return render_template('education.html')

@app.route("/resume")
def resume():
    return render_template('resume.html')
    
@app.route("/contact")
def contact():
    return render_template('contact.html')

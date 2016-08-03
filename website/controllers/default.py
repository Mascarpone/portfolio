# -*- coding: utf-8 -*-
from website import app
from flask import render_template, redirect, url_for, abort, request, flash
from website.models.education import model
from website.models.form import ContactForm
import requests

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
    schools = model.getSchools()
    schoolsnames = model.getSchoolsNames()
    projects = model.getProjects()
    projectsnames = model.getProjectsNames()
    return render_template('education.html', schools=schools, schoolsnames=schoolsnames, projects=projects, projectsnames=projectsnames)

@app.route("/grades")
@app.route("/grades/<filename>")
def grades(filename=None):
    if filename is None:
        return render_template('grades.html')
    grades = model.getDocument(filename)
    return render_template('grades.html', grades=grades)

@app.route("/resume")
def resume():
    return render_template('resume.html')
    
@app.route("/contact", methods=["GET", "POST"])
def contact(other=None): # the use of 'other' is a temporary solution for POST forms compatibility with smoothState
    form = ContactForm()
    if form.validate_on_submit():
        # check the recaptcha
        captcha_response = request.form["g-recaptcha-response"]
        data = {'secret': '***REMOVED***', 'response': captcha_response}
        post_response = requests.post("https://www.google.com/recaptcha/api/siteverify", data = data)
        if post_response.json()['success'] == True:
            # send the email
            flash(u"Your message has been sent")
        else:
            flash(u"Are you a robot?")
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form, other=other)

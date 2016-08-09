# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField, validators
from wtforms.fields.html5 import EmailField

class ContactForm(Form):
    name = StringField('Name', [validators.DataRequired(), validators.length(max=30)], render_kw={"placeholder": "Firstname Surname"})
    email = EmailField('Email address', [validators.DataRequired(), validators.Email()], render_kw={"placeholder": "Email"})
    obj = StringField('Object', [validators.DataRequired(), validators.length(max=50)], render_kw={"placeholder": "Object"})
    text = TextAreaField(None, [validators.DataRequired()], render_kw={"placeholder": "Message ..."})
    
# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask.ext.mail import Mail

app = Flask('website')
app.config.update(
	DEBUG = True,
	SECRET_KEY = '***REMOVED***',
	# EMAIL SETTINGS
	MAIL_SERVER = '***REMOVED***',
	MAIL_PORT = 465, 
	MAIL_USE_SSL = True, 
	MAIL_USE_TLS = False,
	MAIL_USERNAME = '***REMOVED***',
	MAIL_PASSWORD = '***REMOVED***',
	MAIL_DEFAULT_SENDER = '***REMOVED***'
    )

mail = Mail(app)
bdd = "***REMOVED***"

from website.controllers import *
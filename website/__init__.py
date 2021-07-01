import os

from flask import Flask
from flask.ext.mail import Mail


# INIT THE VARS
secret_key = ""
mail_server = ""
mail_port = 0
mail_use_ssl = False
mail_use_tls = False
mail_username = ""
mail_password = ""
mail_default_sender = ""
mail_default_recipients = [""]
data_filename = "data.yml"
g_secret = ""

try:
    from dev_vars import *
except ImportError:
    pass

# APPLICATION CONFIGURATION
app = Flask("website")
app.config.update(
    # APP SETTINGS
    SECRET_KEY=secret_key,
    # EMAIL SETTINGS
    MAIL_SERVER=mail_server,
    MAIL_PORT=mail_port,
    MAIL_USE_SSL=mail_use_ssl,
    MAIL_USE_TLS=mail_use_tls,
    MAIL_USERNAME=mail_username,
    MAIL_PASSWORD=mail_password,
    MAIL_DEFAULT_SENDER=mail_default_sender,
)

mail = Mail(app)

from website.controllers import *

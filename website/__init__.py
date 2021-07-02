import os

from flask import Flask
from flask_mail import Mail


g_secret = ""
data_filename = "data.yml"

try:
    from dev_vars import *
except ImportError:
    pass

app = Flask("website")
app.config["SECRET_KEY"] = os.urandom(32)
mail = Mail(app)

from website.controllers import *

# -*- coding: utf-8 -*-
import os
from flask import Flask

app = Flask('website')
app.debug = True
app.secret_key = 'd0ntW4tch'

bdd = "***REMOVED***"

from website.controllers import *
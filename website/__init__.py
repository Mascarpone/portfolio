# -*- coding: utf-8 -*-
import os
from flask import Flask

app = Flask('website')
app.debug = True

bdd = "***REMOVED***"

from website.controllers import *
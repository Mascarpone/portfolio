# -*- coding: utf-8 -*-
import os
from flask import Flask
app = Flask('website')
app.debug = True

from website.controllers import *
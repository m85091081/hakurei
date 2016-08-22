# -*- coding: utf-8 -*-
# muMDAU_app init file 
# some debug code of server like update/restart code
from flask import Flask , render_template
app = Flask(__name__)
import muMDAU_app.login 
import muMDAU_app.logout 
import muMDAU_app.panel

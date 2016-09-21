# -*- coding: utf-8 -*-
# muMDAU_app main / first page 
from muMDAU_app import app 
from flask import request, render_template, Blueprint, url_for, redirect
from database import EventSQL
main = Blueprint('main', __name__)

# index page main route page 
@main.route('/')
def index():
    elist = EventSQL.listEvent(3)
    if elist == [] :
        E1Name = '尚未決定'  # NOQA
        E1D = '尚未決定'  # NOQA
    if not elist == []:
        E1Name = elist[0][0]  # NOQA
        E2Name = elist[1][0]  # NOQA
        E3Name = elist[2][0]  # NOQA
        E1D = elist[0][1]  # NOQA
        E2D = elist[1][1]  # NOQA
        E3D = elist[2][1]  # NOQA
    return render_template('index.html', **locals())

# -*- coding: utf-8 -*-
# muMDAU_app main / first page 
from muMDAU_app import app 
from flask import request, render_template, Blueprint, url_for, redirect

main = Blueprint('main', __name__)

# index page main route page 
@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass
    else:
        return render_template('index.html')

@main.route('/blog', methods=['GET', 'POST'])
def blog():
    if request.method == 'POST':
        pass
    else:
        return render_template('blog.html')


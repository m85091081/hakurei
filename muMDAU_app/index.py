# -*- coding: utf-8 -*-

from flask import request, render_template, Blueprint

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pass
    else:
        return render_template('index.html')


@main.route('/about', methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        pass
    else:
        return render_template('about.html')

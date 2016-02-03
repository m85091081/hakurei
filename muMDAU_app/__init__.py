# -*- coding: utf-8 -*-

from flask import Flask, request, session, redirect, url_for
from flask import render_template 

app = Flask(__name__)
import subprocess

def restart_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
def gitpull():
    subprocess.call(['git pull'], shell=True)
def pkill_server():
    subprocess.call(['pkill pypy3'], shell=True)

@app.route('/update')
def update():
    if 'username' in session:
        gitpull()
        restart_server()
        return render_template('wait.html')
    else:
        return redirect(url_for('loginp'))

@app.route('/restart')
def restart():
    if 'username' in session:
        restart_server()
        return render_template('wait.html')
    else:
        return redirect(url_for('loginp'))


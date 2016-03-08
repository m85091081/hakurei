# -*- coding: utf-8 -*-

from muMDAU_app import app
from flask import request, session, render_template, url_for, redirect
from database import ManageSQL, countUSER, EventSQL
from subprocess import PIPE
import setting
import os, subprocess

@app.route('/event/add', methods=['GET', 'POST'])
def eadd():
    if request.method == 'POST':
        if 'username' in session:
            name = request.form['name']
            date = request.form['date']
            EventSQL.addEvent(name, date)
            return redirect(url_for('panel'))
        else:
            return 'nologin'

@app.route('/event/del/<ev>', methods=['GET', 'POST'])
def edel(ev):
    if request.method == 'GET':
        if 'username' in session:
            EventSQL.delEvent(ev)
            return redirect(url_for('panel'))
        else:
            return redirect(url_for('panel'))

@app.route('/init', methods=['GET', 'POST'])
def init():
    if request.method == 'POST':
        user = request.form['buser']
        passd = request.form['bpass']
        import hashlib
        hashsha = hashlib.sha256(passd.replace('\n', '').encode())
        ManageSQL.addUser(user, hashsha.hexdigest(), '1', '0')
        return redirect(url_for('panel'))
    else:
        answer = countUSER.countAdmin()
        if answer[0] == 0:
            return render_template('first.html')
        else:
            return redirect(url_for('panel'))

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        blogpath = './hakureinews'
        # check blog repo
        if os.path.exists(blogpath):
            # if blog repo found run pull merge 
            p = subprocess.Popen(['git pull'], shell=True, cwd='./hakureinews', stdout=PIPE)
            outcode, error = p.communicate()
            f = open(setting.s_log, 'ab')
            # add git log to server.log
            f.write(str.encode('INFO:pull_blog:git -- ') + outcode)
            f.close()
            return 'OK'
        else:
            # if blog not found run clone new blog repo
            p = subprocess.Popen(['git clone ' + setting.gitpath], cwd='./', shell=True, stdout=PIPE, stderr=PIPE)
            outcode, gitlog = p.communicate()
            f = open(setting.s_log, 'ab')
            f.write(str.encode('INFO:cloneblog:git -- ') + gitlog)
            f.close()        
            return 'OK'
    else:
        if 'username' in session:
            return render_template('gitload.html')
        else:
            return redirect(url_for('loginp'))

@app.route('/admin/panel')
def panel():
        if 'username' in session:
            elist = EventSQL.listAllEvent()
            return render_template('edit.html', **locals())
        else:
            return redirect(url_for('loginp'))


@app.route('/panel/server', methods=['GET', 'POST'])
def maintance():
    if request.method == 'GET':
        if 'username' in session:
            f = open(setting.s_log)
            return render_template('log.html', log=f.read())
        else: 
            return redirect(url_for('loginp'))

@app.route('/panel/rmlog', methods=['GET', 'POST'])
def rmlog():
    if request.method == 'GET':
        if 'username' in session:
            os.remove(setting.s_log)
            open(setting.s_log, 'a').close()
            return redirect(url_for('restart'))
        else: 
            return redirect(url_for('loginp'))

@app.route('/dev/panel')
def mainten():
    if 'username' in session:
        return render_template('maintenancep.html', username=session['username'])
    else:
        return redirect(url_for('loginp'))

@app.route('/user/panel')
def userp():
    if 'username' in session:
        return render_template('userp.html', username=session['username'])
    else:
        return redirect(url_for('loginp'))

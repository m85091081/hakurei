#!/usr/bin/pypy3
# -*- coding: utf-8 -*-

import sqlite3
import setting as sets

# initialize Database (create table)
class InitDB:
    def createTable():
        try:
            with sqlite3.connect(sets.sqliteFile) as conn:
                cursor = conn.cursor()
                cursor.execute('CREATE TABLE user(username PRIMARY KEY, password, admin ,flogin)')
                cursor.execute('CREATE TABLE date(name PRIMARY KEY, datetime)')
                conn.close
                return True
        except:
            conn.close
            return False

# User Login related function
class LoginSQL:
    def getPass(user):
        try:
            with sqlite3.connect(sets.sqliteFile) as conn:
                cursor = conn.cursor()
                cursor.execute('select password from user where username=?', [user])
                password = cursor.fetchone()
                conn.close
        except:
            conn.close
            password = False
        return password

# counting how many user or admin in database
class countUSER:
    def countAdmin():
        try:
            with sqlite3.connect(sets.sqliteFile) as conn:
                cursor = conn.cursor()
                cursor.execute('select count(*) as numers from user where admin = 1')
                usercount = cursor.fetchone()
                conn.close
        except:
            conn.close
            usercount = False 
        return usercount
    def countUser():
        try:
            with sqlite3.connect(sets.sqliteFile) as conn:
                cursor = conn.cursor()
                cursor.execute('select count(*) as numers from user')
                usercount = cursor.fetchone()
                conn.close
        except:
            conn.close
            usercount = False 
        return usercount

# Managment using function
class ManageSQL:
    def addUser(user, password, admin, first):
        try:
            with sqlite3.connect(sets.sqliteFile) as conn:
                values = [(str(user), str(password), int(admin), int(first)), ]
                print(conn.executemany('INSERT INTO user VALUES (?,?,?,?)', values))
                conn.commit()
                conn.close
                return True
        except:
            conn.close
            return False

    def setAdmin(username, admin):
        try:
            with sqlite3.connect(sets.sqliteFile) as conn:
                values = [(admin, username), ]
                conn.executemany('UPDATE user SET admin=? WHERE username=?', values)
                conn.commit()
                conn.close
                return True
        except:
            conn.close
            return False 

    def setPassword(username, password):
        try:
            with sqlite3.connect(sets.sqliteFile) as conn:
                values = [(password, username), ]
                conn.executemany('UPDATE user SET password=? WHERE username=?', values)
                conn.commit()
                conn.close
                return True
        except:
            conn.close
            return False 

    def setFirst(username, first):
        try:
            with sqlite3.connect(sets.sqliteFile) as conn:
                cursor = conn.cursor()
                values = [(first, username), ]
                cursor.execute('UPDATE user SET flogin=? WHERE username=?', values)
                data = cursor.fetchall()
                conn.close
                return data
        except:
            conn.close
            return False

    def listUser():
        try:
            with sqlite3.connect(sets.sqliteFile) as conn:
                cursor = conn.cursor()
                cursor.execute('select username from user')
                data = cursor.fetchall()
                conn.close
                return data
        except:
            conn.close
            return False

## Event related SQL
class EventSQL:
    def addEvent(name,date):
        try:
            with sqlite3.connect(sets.sqliteFile) as conn:
                values = [(str(name), str(date)), ]
                print(conn.executemany('INSERT INTO date (name,datetime) VALUES (?,?)', values))
                conn.commit()
                conn.close
                return True
        except:
            conn.close
            return False

    def listEvent(count):
        try:
            with sqlite3.connect(sets.sqliteFile) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT * from date ORDER BY datetime DESC LIMIT '+str(int(count)))
                data = cursor.fetchall()
                conn.close
                return data
        except:
            conn.close
            return False

    def setDate(name, date):
        try:
            with sqlite3.connect(sets.sqliteFile) as conn:
                values = [(date, name), ]
                conn.executemany('UPDATE date SET datetime=? WHERE name=?', values)
                conn.commit()
                conn.close
                return True
        except:
            conn.close
            return False 

    def delEvent(name):
        try:
            with sqlite3.connect(sets.sqliteFile) as conn:
                cursor = conn.cursor()
                values = [(name), ]
                cursor.execute('delete from date WHERE name=?',values)
                cursor = conn.cursor()
                conn.commit()
                conn.close
                return True
        except:
            conn.close
            return False 


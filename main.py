#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, url_for, request, redirect, jsonify, send_from_directory
from flask_login import LoginManager, login_user, current_user, logout_user, login_required, UserMixin
from flask_socketio import SocketIO, emit
from flask_sqlalchemy import SQLAlchemy
from getmac import get_mac_address
from flask_bcrypt import Bcrypt
import json, string, random
from datetime import datetime, timedelta
from SMS import SMS
from socket import *
import platform
import psutil
import shutil
import requests
import pandas
import numpy
import os
import ssl
import hashlib

host='192.168.0.56'
port=100

db_name = 'Dongdaegu2'
db_ip = '192.168.0.11'

server_public_port=port
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://asi:asiasi@'+db_ip+'/'+db_name
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)
login_manager.login_view = 'login'
socketio = SocketIO(app)
sms = SMS()

def get_hash(plain_password, user_email):
    key = plain_password + '-----' + str(user_email)
    print(key)
    return hashlib.sha256(key.encode()).hexdigest()


@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    name = db.Column(db.String(25), unique=False, nullable=False)
    last_name = db.Column(db.String(25), unique=False, nullable=False)
    sex = db.Column(db.String(1), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone_number = db.Column(db.String(13), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    level = db.Column(db.Integer, nullable=False, default=0)


@app.route("/",methods=['GET', 'POST'])
@app.route("/login.html",methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route("/<destination>",methods=['GET', 'POST'])
def Main(destination):
    return render_template('layout.html')


@app.route("/Logout.html")
def logout():
    return redirect('login.html')

if __name__ == "__main__":
    socketio.run(app, host=host, port=port, debug=True)

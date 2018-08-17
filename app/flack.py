import os

from flask import Flask, render_template, jsonify, request, url_for, redirect
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

users = {}

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'GET':
        if session.get('username') is None or session['username'] == "":
            loggedin = False
            return redirect(url_for('login'))
        else:
            loggedin = True
            return render_template("index.html")
#logging in from login.html to index.html
    elif request.method == 'POST':
        if request.form['password'] == users[request.form['username']]:
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        else:
            return redirect(url_for('login'))

@app.route("/login", methods=['GET','POST'])
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template('register.html')

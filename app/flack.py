import os

from flask import Flask, render_template, jsonify, request, url_for, redirect, session, flash
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)
app.secret_key = 'adamiscool'

users = {"admin":"adminpass"}

@app.route("/", methods=['GET','POST'])
def index():
    if request.method == 'GET':
        if session.get('username') is None or session['username'] == "":
            return redirect(url_for('login'))
        else:
            return render_template("index.html", username = session['username'])
    elif request.method == 'POST':
        if request.form['password'] == users[request.form['username']]:
            session['username'] = request.form['username']
            return redirect(url_for('index'))
        else:
            flash("Login failed")
            return redirect(url_for('login'))

@app.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    elif request.method == 'POST':
        if request.form['username'] not in users:
            users[request.form['username']] = request.form['password']
            flash("Account registered, " + request.form['username'])
            return redirect(url_for("login"))
        else:
            flash("Username in use")
            return redirect(url_for("register"))

@app.route("/register")
def register():
    return render_template('register.html')

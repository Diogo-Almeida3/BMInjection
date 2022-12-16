from app import app

import database

from flask import render_template, request, url_for, redirect

@app.route("/landing")
def landing():
    return render_template("landing.html")

@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        user = database.login(name, email, password)

        if user:
            return redirect(url_for('landing'))
        else:
            return render_template("login.html")
    
    return render_template("login.html")

@app.route("/signup", methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        success = database.register(name, email, password)
        if success:
            return redirect(url_for('login'))
        return render_template("signup.html")

    return render_template("signup.html")

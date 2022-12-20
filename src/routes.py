
from app import app
from flask import render_template, request, url_for, redirect, make_response, flash
from werkzeug.routing import RequestRedirect
from flask import session
import database
import hashlib


@app.route("/flag", methods=["GET"])
def flag():
    # verify cookie
    cookie = request.cookies.get("cookie")
    if cookie == None:
        flash('please login!', category='error')
        return redirect(url_for('login'))
    flag = []
    with open("../flag.txt") as f:
        flag = f.read()
    return flag

@app.route("/landing", methods=["GET", "POST"])
def landing():
    cookie = request.cookies.get("cookie")
    if cookie == None:
        flash('please login!', category='error')
        return redirect(url_for('login'))

    if request.method == "POST":
        ref = request.form.get("reference")
        hght = request.form.get("height")
        wght = request.form.get("weight")

        bmi = 0
        try:
            # Formula: weight (kg) / [height (m)]2
            bmi = float(wght) / (pow( float(hght), 2))
            bmi = round(bmi, 2)
        except Exception as e:
            print(e, flush=True)
            pass
    else:
        ref = None
        bmi = None
    return render_template("landing.html", ref=ref, bmi=bmi)

@app.route("/", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user, user_id = database.login(email, password)
        print("user", user, flush=True)
        print("user_id", user_id, flush=True)

        if user and user_id is not None:
            cook = hashlib.sha256((email+str(user_id)).encode('utf-8')).hexdigest()
            resp = make_response(render_template("landing.html"))
            # set cookie
            resp.set_cookie("cookie", cook)
            return resp
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

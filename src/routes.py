from app import app
import database
from flask import render_template, request, url_for, redirect

@app.route("/landing", methods=["GET", "POST"])
def landing():
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

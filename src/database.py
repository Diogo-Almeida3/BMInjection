import mysql.connector
from flask import flash
import bcrypt

def connect_db(args=(), one=False):
    cnx = mysql.connector.connect(user='root', password='root', host='db', port="3306", database='BMInjection')
    return cnx

def query_db(query, args=(), one=False):
    cnx = connect_db()
    cursor = cnx.cursor()
    rows = []
    try:
        cursor.execute(query, args)
        # process
        rows = cursor.fetchall()
    except Exception as e:
        print(e, flush=True)
    return rows

def insert_db(query, args=(), one=False):
    cnx = connect_db()
    cursor = cnx.cursor()
    try:
        cursor.execute(query, args)
        cnx.commit()
    except Exception as e:
        print(e, flush=True)
        return False
    return True

def login(name, email, password):
    user = []
    user = query_db('SELECT pass FROM USERS WHERE email = %s', (email, ), one=True)

    if user:
        passhash = user[0][0]
        pass_check =  verify_hash(password, passhash)
        if pass_check:
            flash('Logged in successfully!', category='success')
            return True
        else:
            flash('Wrong credentials, try again...', category='error')
            return False
    else:
        flash('Wrong credentials, try again...', category='error')
        return False

def register(name, email, password):
    result = query_db('SELECT * FROM USERS WHERE email = %s', (email, ), one=True)

    if result:
        flash('Email already in use, pls try again with diferent email!', category='error')
        return False
    hashed = generate_password_hash(password)

    insert_db('INSERT INTO USERS (username, email, pass) VALUES (%s, %s, %s)', (name, email, hashed), one=True)
    flash('Registration was successful!', category='success')
    return True

def generate_password_hash(password):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode()

def verify_hash(password, passhash):
    return bcrypt.checkpw(password.encode(), passhash.encode())
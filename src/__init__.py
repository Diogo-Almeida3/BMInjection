from flask import Flask, request
import json
import mysql.connector
from flask_cors import CORS
from flask import jsonify
import ast

def create_app():
    #Set mysql access credentials 
    file = open("credentials", "r")
    content = file.read()
    config = ast.literal_eval(content)
    file.close()

    app = Flask(__name__)
    CORS(app)

    from .auth import  auth
    app.register_blueprint(auth, url_prefix="/")

    

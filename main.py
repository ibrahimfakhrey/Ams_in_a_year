
from flask import Flask, render_template, redirect, url_for, flash, abort
from datetime import date
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
import os

app = Flask(__name__)
app.config['SECRET_KEY'] =os.environ.get("SECRET_KEY")


@app.route('/')
def start():
    return render_template("index.html")









if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
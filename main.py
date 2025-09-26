import datetime
from flask import Flask, render_template, url_for
from collections import defaultdict

import psycopg2

app = Flask(__name__)
DATABASE_PASSWORD=""

def get_db_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="codecortex",
        user="postgres",
        password=DATABASE_PASSWORD
    )

    return conn



@app.route("/")
def home():
    return render_template(
        "index.html",
        year=datetime.date.today().year,
    )

@app.route("/patient")
def patient():
    return render_template(
        "patient.html"
    )

@app.route("/caretaker")
def caretaker():
    return render_template(
        "caretaker.html"
    )

if __name__ == "__main__":
    app.run(debug=True)

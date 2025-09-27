import datetime

from flask import Flask, render_template

app = Flask(__name__)


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

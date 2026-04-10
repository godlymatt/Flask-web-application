from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config['SESSION_PERMANENT'] = True
app.config['SESSION_TYPE'] = "filesystem"

Session(app)

shows = {}

@app.route('/')
def title_page():
    if "shows" not in session:
        flash("Welcome in have a seat and add your favourite shows!")
    return render_template("main.html")


@app.route('/form')
def grabbing():
    return render_template('form.html')



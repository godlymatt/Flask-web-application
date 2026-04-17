from flask import Flask, render_template, request, session, flash
from flask_session import Session
import os

app = Flask(__name__)

app.config['SESSION_PERMANENT'] = True
app.config['SESSION_TYPE'] = "filesystem"

Session(app)

posterSaveLocation = "images"
allowed_types = [".png", ".jpg", ".gif", ".webp"]

shows = {}

@app.route('/')
def title_page():
    if "shows" not in session:
        flash("Welcome in have a seat and add your favourite shows!")
    return render_template("home.html")


@app.route('/form')
def grabbing():
    return render_template('form.html')

@app.route('/hello', methods=['POST'])
def adding():
    showName = request.form['name']
    favCharacter = request.form['char']
    summary = request.form['sum']
    startingYear = request.form['start']
    poster = request.files['showPic']
    if poster.filename != '':
        savePosterName = os.path.join(posterSaveLocation, poster.filename)
        poster.save(savePosterName)
    
    if "shows" in session:
        session["shows"][showName] = {"Favourite Character":favCharacter, "Summary":summary, "Starting year":startingYear, "poster":poster.filename}

    else:
        session["shows"] = {}
        session["shows"][showName] = {"Favourite Character":favCharacter, "Summary":summary, "Starting year":startingYear, "poster":poster.filename}

    flash(f"Show {showName} has been added!")
    return render_template('form.html')

@app.route('/display')
def displaying():
    print(session)
    return render_template('display.html', shows = session.get("shows", {}), posterLocation = posterSaveLocation)

@app.route('/remove', methods=['GET', 'POST'])
def remove_show():
    shows = session.get("shows", {})

    if request.method == 'POST':
        selected_show = request.form.get('show_name')
        if selected_show and selected_show in shows:
            shows.pop(selected_show, None)
            if shows:
                session["shows"] = shows
            else:
                session.pop("shows", None)
            session.modified = True
            flash(f"Show {selected_show} has been removed.")
        else:
            flash("Please select a valid show to remove.")

    return render_template('remove.html', shows=shows)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
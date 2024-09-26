from flask import Flask, render_template, request
from config import Config
import sqlite3
import random

app=Flask(__name__)
app.config.from_object(Config)


# Get the title of the website from Config and
# make it available to all templates. Used in
# header.html and layout.html in this case
@app.context_processor
def context_processor():
  return dict(title=app.config['TITLE'])


# The home page
@app.route('/')
def home():
  return render_template('home.html')


# Displays all teddys in the database
# TODO: link each teddy to its own details page
@app.route('/all_wools')
def all_wools():
    # This boilerplate db connection could (should?) be in
    # a function for easy re-use
    conn = sqlite3.connect(app.config['DATABASE'])
    cur = conn.cursor()
    cur.execute("SELECT * FROM Wool ORDER BY id;")
    # fetchall returns a list of results
    wools = cur.fetchall()
    conn.close()  # always close the db when you're done.
    # print(wools)  # DEBUG
    return render_template("all_wools.html", wools=wools)


# Individual wool details page.
@app.route('/wool/<int:id>')
def wool_details(id):
  # print("The wool id is {}".format(id))  # DEBUG
  conn = sqlite3.connect(app.config['DATABASE'])
  cur = conn.cursor()
  cur.execute("SELECT * FROM Teddy WHERE id=?;",(id,))
  # fetchone returns a tuple containing the data for one entry
  wool = cur.fetchone()
  conn.close()
  return render_template("wool.html", wool=wool)


# about Woolly Wishes
@app.route('/about')
def about():
  formstuff = None
  if len(request.args) > 0:
    formstuff = []
    formstuff.append(request.args.get('username'))
    formstuff.append(request.args.get('password'))
  return render_template('about.html', formstuff=formstuff)


if __name__ == '__main__':
  app.run(debug=app.config['DEBUG'], port=8080, host='0.0.0.0') 
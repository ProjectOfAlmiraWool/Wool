from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/all_wools')
def all_wools():
    conn = sqlite3.connect('wool.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Wool")
    wools = cur.fetchall()
    conn.close()
    return render_template('all_wools.html', wools=wools)
  
@app.route('/sizes')
def sizes():
    conn = sqlite3.connect('woold.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Wool")
    sizes = cur.fetchall()
    conn.close()
    return render_template('sizes.html', sizes=sizes) 

if __name__ == '__main__':
    app.run(debug=True)

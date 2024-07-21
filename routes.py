from flask import Flask, redirect, url_for 

app = Flask(__name__)

@app.route("/") 
def home():
  return "Welcome! this is wooly wishes <h1>WELCOME<h1>"

@app.route("/<name>")
def user(name):
  return f"Welcome {name}!"

@app.route("/admin")
def admin():
  return redirect(url_for("home")) 

if __name__ == "__main__":
  app.run()
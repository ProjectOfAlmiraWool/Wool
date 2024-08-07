from flask import Flask, redirect, url_for, render_template, request, session, flash  
from datetime import timedelta


app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(days=1)


@app.route("/<name>")
def home(name):
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
  if request.method == "POST":
    session.permanent = True
    user = request.form["nm"]
    session["user"] = user
    flash("Login Successful!")
    return redirect(url_for("user"))
  else:  
    if "user" in session:
        flash("Already Logged In!")
        return redirect(url_for("user"))    
     
    return render_template("login.html")
   
@app.route("/user", methods=["POST", "GET"])
def user():
    email = None  
    if "user" in session:
        user = session["user"]
       
        if request.method == "POST":
          email = request.form["email"]
          session["email"] = email
          flash("Email was saved!")
        else:
          if "email" in session:
              email = session["email"]  
         
        return render_template("user.html", email=email)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))
   
@app.route("/logout")
def logout():
  if "user" in session:
        user = session["user"]
        flash("You have been logged out!", "info")
  session.pop("user", None)
  session.pop("email", None)
  return redirect(url_for("login"))


if __name__ == "__main__":
  app.run(debug=True)

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    else:
        flash("You are not logged in!")
        return redirect(url_for("login"))

if __name__ == "__main__":
  app.run(debug=True) 
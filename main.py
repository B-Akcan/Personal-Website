from flask import Flask, render_template, request, session, redirect, url_for
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "batuhan"
app.permanent_session_lifetime = timedelta(minutes=30)

@app.route("/home")
@app.route("/")
def home():
    if "user" in session:
        user = session["user"]
        return render_template("home.html", usr=user)
    else:
        return render_template("home.html", usr=None)

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        session["user"] = user
        session.permanent = True
        return redirect(url_for("home"))
    elif "user" in session:
        user = session["user"]

    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home"))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

if __name__ == "__main__":
    app.run(debug=True)

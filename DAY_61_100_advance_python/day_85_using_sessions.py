import os
from flask import Flask, redirect, request, session

app = Flask(__name__)
app.secret_key = os.environ['sessionkey']

@app.route("/")
def index():
  page = ""
  myName = ""
  if session.get("myName"):
    myName = session["myName"]
  page += f"<h1>{myName}</h1>"
  f = open("form.html", "r")
  page = f.read()
  f.close()
  return page


@app.route("/setlogin", methods=["POST"])
def setLogin():
  session["myName"] = request.form["name"]
  return redirect("/")


app.run(host="0.0.0.0", port=81)
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
  if request.headers["X-Replit-User-Name"]:
    return redirect("/home")

  page = ""
  f = open("page.html", "r")
  page = f.read()
  f.close()
  return page

@app.route("/home")
def home():
  if not request.headers["X-Replit-User-Name"]:
    return redirect("/")

  page = ""
  page += f"""<h1>{request.headers["X-Replit-User-Name"]}</h1>"""

  page += f"""<img src="{request.headers["X-Replit-User-Profile-Image"]}" width="200">"""
  
  return page

app.run(host='0.0.0.0', port=81)
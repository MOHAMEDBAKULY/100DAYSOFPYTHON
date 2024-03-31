from flask import Flask

app = Flask(__name__)

mydictionary = {}

mydictionary["78"] = {"date": "March 31st", "Reflection": "I am feeling good"}

@app.route("/<pagenumber>")

def index(pagenumber):
  page = ""
  f = open("template/template.html", "r")
  page = f.read()
  f.close()
  page.repalce("{date}", pagenumber)
  page.repalce("{date}", pagenumber)
  page.repalce("{Reflection}", pagenumber)
  return f"This is page {pagenumber}"


app.run(host="0.0.0.0", port=81)
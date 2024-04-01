
from flask import Flask, request

app = Flask(__name__)

logins = {}
logins["Maryam"] = {"email": "maiya@gmail.com", "password": "Chapa"}
logins["Younos"] = {"email": "YU@gmail.com", "password": "BabaYu"}
logins["Aisha"] = {"email": "Isha@gmail.com", "password": "Mamaisha"}
logins["Bakuly"] = {"email": "Bakuly@gmail.com", "password": "bakuly"}

@app.route("/login", methods=["POST"])
def login():
  form = request.form
  isThere = False
  details = {}
  try:
    details = logins[form["username"]]
    isThere = True
  except:
    if form["email"] == details["email"] and form["password"] == details["password"]:
      return "You are logged in"
    else:
      return "Username, email or password incorrect"
      return "Username, email or password incorrect"


@app.route('/')
def index():
  page = """<form method = "post" action="process">
    <p>Name: <input type="text" name="username" required> </p>
    <p>Email: <input type="Email" name="email"> </p>
    <p>Password: <input type="password" name="password"> </p>
    <input type="hidden" name="userID" value="232"> </p>

    <p>
      Fave Baldy: 
      <select name="baldies">
        <option value="younos">Younus</option>
        <option value="maryam">Maryam</option>
        <option value="aisha">Aisha</option>
        <option value="mohammed">Mohammed</option>
      </select>
    </p>

    <button type="submit">Save Data</button>
  </form>


    """
  return page

app.run(host='0.0.0.0', port=81)
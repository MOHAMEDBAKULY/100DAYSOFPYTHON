from  flask import Flask, request

app = Flask(__name__)


@app.route('/questions', methods=['POST'])
def questions():
  form = request.form
  if form['text'] == 'Yes':
    return 'Hello robot'
  elif 'Error' in form['infinity'].lower():
    return 'Hello Robocom'
  elif form['games'] == 'Minecraft':
    return 'Hello Minecraft'
  else:
    return "Hi there murkomen"


@app.route('/')
def index():
  page = ""
  f = open("forms.html", "r")
  page = f.read()
  f.close()
  return page


app.run(host='0.0.0.0', port=81)
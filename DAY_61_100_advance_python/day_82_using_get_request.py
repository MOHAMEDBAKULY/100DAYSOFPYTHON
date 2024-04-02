from flask import Flask ,request

app = Flask(__name__)


@app.route('/language', methods=["GET"])
def lang():
  data = request.args
  if data == {}:
    return "Nothing here"
  if data["lang"] == "eng":
    return "Is lubnah my soulmate, I really love her soo much"
  elif data['lang'] == "kis":
    return "Je, Lubnah ni mwenzi wangu wa roho?, Nampenda sana"


@app.route('/', methods=["GET"])
def kiswahili():
  return "Welcome"


app.run(host='0.0.0.0', port=81)
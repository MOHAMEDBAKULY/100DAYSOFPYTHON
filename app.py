from my_flask_file import Flask

app = Flask(__name__, static_url_path = "/static")

@app.route('/')
def home():
    myName = "Bakuly"
    page = f"How is Ramadhan on going {myName}"
    return page


app.run(host = "0.0.0.0", port = 81)
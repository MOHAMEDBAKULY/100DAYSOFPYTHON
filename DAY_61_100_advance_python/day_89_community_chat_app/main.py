from flask import Flask, redirect, request
import datetime
# from replit import db

app = Flask(__name__)

@app.route('/')
def index():
  
  page = ""
  f = open('chat.html', 'r')
  page = f.read()
  f.close()
  page = page.replace('{username}', request.headers['X-Replit-User-Name'])
  return page

@app.route('/add', methods=['POST'])
def add():
  form = request.form
  message = form['message']
  date = datetime.datetime.now()
  timestamp = datetime.datetime.timestamp(date)
  userId = request.headers['X-Replit-User-Id']
  username = request.headers['X-Replit-User-Name']
  # db[timestamp] = {"userId": userId, "username": username, "message": message}
  # page = f"""{userId} {username} {timestamp} 
  # {message}"""
  return redirect('/')
  

app.run(host='0.0.0.0', port=81)
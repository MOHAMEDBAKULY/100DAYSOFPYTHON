import random
# from replit import db

def createUser():
    username = input("Username > ")
    password = input("Password > ")
    # # keys = db.keys()
    # if username in keys:
    #     print("ERROR: Username exists")
    #     return
      
    salt = random.randint(1000,9999)
    newPassword = f"{password}{salt}"
    newPassword = hash(newPassword)

    # db[username] =  {"password": newPassword,
                    #  "salt": salt}
    print("Password has been added")
  
def login():
   username = input("Username > ")
   password = input("Password > ")
#    keys = db.keys()
#    if username not in keys:
#       print("ERROR: Username does not exists")
#       return

#    salt = db[username]["salt"]
#    newPassword = f"{password}{salt}"
   newPassword = hash(newPassword)


# #    if db[username]["password"]==newPassword:
#       print("Login successful")
#    else:
#       print("Username or password incorrect")
#       print("Welcome to the secret diary")



  
while True:
  menu = input("1: Add User, 2: Login >")
  if menu == "1": 
    createUser()
  elif menu == "2":
    login()
  else:
    print("Please Enter 1 or 2")
    # keys = db.keys()
    # for key in keys:
    #   print(db[key])




# userName = "Bakuly"
# password = "MUIRA2020WEST/."
# password = hash(password)
# db[userName] = password
# print(db["Bakuly"])
# ask = input("Password > ")
# ask = hash(ask)
# if ask == db["Bakuly"]:
#   print("Welcome back")

# password = "Bakuly"
# salt = 7233
# newPassword = f"{password}{salt}"
# newPassword = hash(newPassword)

# print(newPassword)


# password = "Bakulain"
# salt = 7033
# newPassword = f"{password}{salt}"
# newPassword = hash(newPassword)

# print(newPassword)
# db["Bakuly"] = {"Password": newPassword, "Salt": salt}

# ask = input("Password > ")
# salt = db["Bakuly"]["Salt"]
# newPassword = f"{ask}{salt}"
# newPassword = hash(newPassword)
# if newPassword == db["Bakuly"]["Password"]:
#      print("log in was successful")
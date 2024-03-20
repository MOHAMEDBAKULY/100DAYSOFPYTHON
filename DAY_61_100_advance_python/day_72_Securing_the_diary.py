# from replit import db
# import time, os, datetime, random

# print("Thoughts are precious welcome to my Private diary")
# print()

# del db["username"]

# def addToDiary():
#   print("Create your diary")
#   title = input("Title: ")
#   thought = input("Thought: ")
#   emotion = input("Emotion or feeling: ")
#   timestamp = datetime.datetime.now()
#   db[timestamp] = {"Entry title": title, "Entry thought": thought, "Entry emotion": emotion}
#   print("Thanks for sharing your thoughts")


# def viewDiary():
#   matches = db.prefix("timestamp")
#   matches = matches[::-1]
#   keys = db.keys() 
#   for key in keys:
#    time.sleep(1)
#    os.system("clear")
#    print(f"""{keys}: {db[key]}""")
#    print()
#    action = input("Next or exit? > ")
#    if(action.lower()[0]=="e"):
#       break




# keys = db.keys()
# if len(keys) < 1:
#    print("Create password and username for your diary")
#    username = input("Username: ")
#    password = input("Password: ")
#    salt = random.randint(1000,9999)
#    newpassword = hash(f"{password}{salt}")
#    db[username] = {"Password": newpassword, "Salt": salt}
#    print("Password has been created")
# else:
#   print("Login into account")
#   username = input("Username: ")
#   password = input("Password: ")
#   if username not in keys:
#     print("ERROR:username does not exist")
#     exit()
#   salt = db[username]["salt"]
#   newpassword = hash(f"{password}{salt}")
#   if db[username]["password"] != newpassword:
#     print("ERROR:password is incorrect")
#     exit()


# while True: 
#   userInput = input("""Actions to use the Diary
#     1. Add
#     2. View
#     3. Exit
#     your action:> """)

#   if userInput == "1":
#      addToDiary()
#   elif userInput == "2":
#     viewDiary()
#   elif userInput == "3":
#     break
#   else:
#     print("Wrong input: enter 1, 2 or 3")
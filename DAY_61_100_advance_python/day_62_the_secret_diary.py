# from replit import db
import time, os, datetime, random



print("Thoughts are precious welcome to my Private diary")
print()

secret_diary = {}
password = random.randint(1,5)

def addToDiary():
  title = input("Title: ")
  thought = input("Thought: ")
  emotion = input("Emotion or feeling: ")
  timestamp = datetime.datetime.now()
  row = {"Time": timestamp , "Entry title": title, "Entry thought": thought, "Entry emotion": emotion}
  secret_diary.append(row)
  print("Thanks for sharing your thoughts")


#   matches = db.prefix("timestamp")
#    time.sleep(1)
#   matches = matches[::-1]
#   keys = db.keys() 
#    os.system("clear")
#    print(f"""{keys}: {db[key]}""")

def viewDiary():
  for row in secret_diary:
      for item in row:
          print(item) 
      print()
      action = input("Next or exit? > ")
      if(action.lower()[0]=="e"):
        break

enterPassword = int(input("Enter the password: "))
if enterPassword == password:
  print("Welcome to my diary")
elif enterPassword != password:
  print("Wrong password")
  exit()
  
while True: 
  userInput = input("""Actions to use the Diary
    1. Add
    2. View
    3. Exit
    your action:> """)
  
  if userInput == "1":
     addToDiary()
  elif userInput == "2":
    viewDiary()
  elif userInput == "3":
    break
  else:
    print("Wrong input: enter 1, 2 or 3")
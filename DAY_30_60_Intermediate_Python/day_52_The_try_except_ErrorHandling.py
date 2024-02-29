import time, os 

pizzaOrder = []

try:
  file = open("pizzaOrder.txt", "r")
  pizzaOrder = eval(file.read())
  file.close()
except:
  print("ERROR: No existing pizza list, using a blank list")


def addPizza():
  print("What is the type of pizza would you have? ")
  userName = input("What is your name?:  ")
  Topping = input("What topping would you like?:  ")
  Size = input("Size of the pizza (s)mall, (m)edium, or (l)arge: ").lower()
  while True:
   try:
    Quantity = int(input("How many pizzas would you like?:  "))
    break
   except:
    print("You must input a numerical character, try again.")
  cost = 0
  if Size == "s":
    cost = 20.99
  elif Size == "m":
    cost = 23.99
  elif Size == "l":
    cost = 25.99
  Total = cost * Quantity
  Total = round(Total, 2)
  
  row = [userName, Topping, Size, Quantity, Total]

  if row in pizzaOrder:
    print("You have already ordered this pizza")
  else:
    pizzaOrder.append(row)
  time.sleep(2)
  os.system("clear")
  

def viewPizzas():
  print("Which Pizza order would you like to view?")
  for row in pizzaOrder:
    for item in  row:
      print(f"{item: ^10}", end = " | ")
    print()
  time.sleep(10)
  os.system("clear")

  

while True:
  print("Welcome to the Pizza Shop!")
  userInput = input("""
            In my Pizza Shop you have two options:
            1. Add a pizza
            2. View your order
            3. Exit
            Input your choice: > """)
  if userInput == "add":
    addPizza()
  elif userInput == "view":
    viewPizzas()
  elif userInput == "exit":
    break

  file = open("pizzaOrder.txt", "w")
  file.write(str(pizzaOrder))
  file.close()
  
    





# progressSoFar = []

# try:
#   f  = open("progress.txt", "r")
#   progressSoFar = eval(f.read())
#   f.close()
# except Exception as err:
#   print("We have a problem on our side")
#   print(err)


# for row in progressSoFar:
#   print(row)

# debugMode = False

# newYearResolutions = []

# try:
#   f = open("newYearResolutions.txt", "r")
#   newYearResolutions = eval(f.read())
#   f.close()
# except Exception:
#   print("We have a problem on our side wait as we resolve it")
#   if debugMode:
#    print(traceback)

# for row in newYearResolutions:
#   print(row)

# my2Dlist = []

# try:  
#  f = open("Stuff.mine","r")
#  myStuff = eval(f.read())
#  f.close()
# except Exception as err:
#  print(err)
#  print("We have problmes on our side")

# for row in my2Dlist:
#   print(row)
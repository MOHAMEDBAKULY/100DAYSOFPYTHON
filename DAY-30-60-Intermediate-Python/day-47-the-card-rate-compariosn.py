
import os, time, random

trumps = {}
trumps["David"] = {"Intelligence": 178, "Speed": 4, "Guile": 80, "Baldness Level": 99}
trumps["Mr Spock"] = {"Intelligence": 200, "Speed": 50, "Guile": 50, "Baldness Level": 0}
trumps["Moica from Friends"] = {"Intelligence": 150, "Speed": 50, "Guile": 50, "Baldness Level": 0}
trumps["Professor X"] = {"Intelligence": 250, "Speed": 1, "Guile": 200, "Baldness Level": 101}

while True:
  print("TOP TRUMPS")
  print()
  print("Characters")
  print()
  for key in trumps:
    print(key)
  user = input("Pick your character\n> ")
  comp = random.choice(list(trumps.keys()))
  print("Computer has picked", comp)

  print("Choose your stat: Intelligence, Speed, Guile & Baldness Level")

  answer = input("> ")

  print(f"{user}: {trumps[user][answer]}")
  print(f"{comp}: {trumps[comp][answer]}")

  if trumps[user][answer] > trumps[comp][answer]:
    print(user, "wins")
  elif trumps[user][answer] < trumps[comp][answer]:
    print(comp, "wins")
  else:
    print("Draw")


  time.sleep(2)
  os.system("clear")












# import time, os

# print("Welcome to the Top Trumps 'Best football player Generator")
# print()

# # Create a dictionary for the card
# card = {}
# score = 0

# def preetyPrint():
#    print()
#    for key, value in card.items():
#      print(key, end=": ")
#      for subkey, subvalue in value.items():
#        print(subkey, subvalue, end=" | ")
#    print()

# print('Who is the best player in the world: ')
# print()

# def playerOne():
#   print("Player one make your choice: ")
#   print()
#   name = input("The player's name: ")
#   team1 = input("The player's team: ")
#   ballonDor1 = int(input("Number of Ballon D'or won: "))
#   trophies1 = int(input("Number of trophies won: "))
#   goals1 = int(input("Total goals scored: "))
#   card[name] = {"Team": team1, "Ballon D'or": ballonDor1, "Trophies": trophies1, "Goals": goals1}
#   preetyPrint()
#   time.sleep(2)
#   os.system("clear")

# def playerTwo():
#   print("Player two make your choice: ")
#   print()
#   name = input("The player's name: ")
#   team2 = input("The player's team: ")
#   ballonDor2 = int(input("Number of Ballon D'or won: "))
#   trophies2 = int(input("Number of trophies won: "))
#   goals2 = int(input("Total goals scored: "))
#   card[name] = {"Team": team2, "Ballon D'or": ballonDor2, "Trophies": trophies2, "Goals": goals2}
#   preetyPrint()
#   time.sleep(2)
#   os.system("clear")

  
  
# playerOne()
# playerTwo()



# if card[name]["ballonDor1"] > card[name]["ballonDor2"]:
#    print("Player one wins")
# elif card[name]["ballonDor2"] > card[name]["ballonDor1"]:
#    print("Player two wins")
# else:
#    print("It's a draw")
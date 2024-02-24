# import time, os
# listOfEmails = []

# def preetyPrint():
#   os.system('clear')
#   print('List of Emails')
#   print()
#   counter = 1
#   for email in listOfEmails:
#     print(f"{counter}: {email}")
#   time.sleep(1)


# while True:
#   print('Spamming Filter!!')
#   menu = input('1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ')
#   if menu == '1':
#     email = input('Email > ')
#     listOfEmails.append(email)
#   elif menu == '2':
#     email = input('Email > ')
#     if email in listOfEmails:
#       listOfEmails.remove(email)
#   elif menu == '3':
#     preetyPrint()
#   time.sleep(1)
#   os.system('clear')

# import time, os
# listOfPlayers = []

# def preetyPrint():
#   os.system('clear')
#   print('The list of players in the Team')
#   print()
#   for index in range(len(listOfPlayers)):
#     print(f"{index}: {listOfPlayers[index]}")
#   time.sleep(2)

# while True:
#   print("Players Informations")
#   getInfo = input('Press 1 to add a player\nPress 2 to remove a player\nPress 3 to see all players\nStart >. ')
#   if getInfo == '1':
#     player = input('Player Name > ')
#     listOfPlayers.append(player)
#   elif getInfo == '2':
#     player = input('Player Name > ')
#     if player in listOfPlayers:
#       listOfPlayers.remove(player)
#     else:
#       print(f"{player} is not in the list")
#   elif getInfo == '3':
#    preetyPrint()
#   time.sleep(2)
#   os.system('clear')

import os, time
listOfEmail = []

def prettyPrint():
#   os.system("clear") 
  print("listofEmail") 
  print()
  for index in range(len(listOfEmail)): 
    print(f"{index}: {listOfEmail[index]}") 
  time.sleep(1)

def spamPrint(max):
#   os.system("clear")
  print('A list of Spamming Emails')
  print()
  for index in range(0, max):
    print()
    
    print(f""" Email {index + 1} Dear {listOfEmail[index]},\nIt has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.\n\nLove and hugs,\nIan Spammington III""")
    time.sleep(2)
    # os.system("clear")


while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
    else:
      print(f"{email} is not in the list")
  elif menu == "3":
    prettyPrint() 
  elif menu == "4":
    spamPrint(10)
  time.sleep(1)
#   os.system("clear")
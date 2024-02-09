
# myProgram = [];

# def printProgram():
#   print()
#   for item in myProgram:
#     print(item)
#     print()
    
# def addProgram():
#    for i in range(1, 30):
#     print("Is Program", i)

# while True:
#   menu = input("Do you want to add or remove a program tomorrow?: ")
#   if menu == "add":
#     item = input('What is your program tomorrow:? ')
#     myProgram.append(item)
#   elif  menu == "remove":
#     item = input("What program do you want to remove:? ")
#     if item in myProgram:
#      myProgram.remove(item)
#     else:
#       print(f"{item} is not in the list")
#   printProgram()
# myPartyList = []

# def printList():
#   print() 
#   for item in myPartyList:
#     print(item)
#   print() 

# while True:
#   menu = input("Do you want to add or remove someone in the Party: ")
#   if menu == "add":
#     item = input("Who should I add to the party list?: ")
#     myPartyList.append(item)
#   elif menu == "remove":
#     item = input("Who should I remove from the party list?: ")
#     if item in myPartyList:
#       myPartyList.remove(item)
#     else:
#       print(f"{item} was not in the list")
#   printList()

listManager = []
blue = "\033[34m"
reset = "\033[0m"

def printList():
 for item in listManager:
  print(item)
  print()



while True:
  list = input("Do you want to view, add, remove or edit the todo list?: ")
  if list == "view":
    item = input("What item do you want to view?: ")
    printList()
  elif list == "add":
    item = input("What do you want to add?: ")
    listManager.append(item)
  elif list == "edit":
    item = input("What do you want to edit?: ")
    new = input("Replace it with something new?: ")
    for i in range(0, len(listManager)):
      if listManager[i] == item:
        listManager[i] = new
  elif list == "remove":
    item = input("What do you want to remove?: ")
    listManager.remove(item)
    if list in listManager:
      listManager.remove(list)
    else:
      print(f"{list} was not in the list")
  printList()
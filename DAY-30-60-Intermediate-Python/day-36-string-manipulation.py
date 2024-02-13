# name = input("What is your fisrt Name:? ")

# if name.lower().strip() == "mohamed rashid":
#  print('We are missing you so Much')
# else:
#  print("This is not your name")
# import time, os
# myList = []

# def printList():
#   print()
#   for i in myList:
#     print(i)
#   print()

# def removeList():
#   activity = input('What item do you want to remve?:  ')
#   print(f'Are you sure you want to remove {activity} from your list? ')
#   if activity == 'yes':
#     myList.remove(activity)
#   else:
#     print('No item will be removed')

# def editList():
#   activity = input('What do you want to edit?: ')
#   new = input('What do you want to change it to?: ')
#   for i in range(0, len(myList)):
#     if myList[i] == activity:
#       myList[i] = new
#       print(f"This is the new item{new}")

# while True:
#   yourList = input("""
#   1: add list
#   2: remove list
#   3: view list
#   4: edit list
#   5: delete list
#   Start Playing with your list: """).lower().strip()
#   if yourList == "1":
#    activity = input('What do you want to add?: ')
#    myList.append(activity)
#   elif yourList == "2":
#     removeList()
#   elif yourList == "3":
#     printList()
#   elif yourList == "4":
#    editList()
   
# myList = []

# def printList():
#    print()
#    for i in myList:
#      print(i)
#    print()

# while True:
#    addItem = input("Item > ").strip().capitalize()
#    if addItem not in myList:
#      myList.append(addItem)
#    printList()

# myList = []

# def printList():
#  print()
#  for i in myList:
#    print(i)
#  print()

# while True:
#  addItem = input("Item > ").strip().capitalize()
#  if addItem not in myList:
#    myList.append(addItem)
#  printList()

NameList = []

def displayName():
  print('This are your Names')
  print()
  for index in range(len(NameList)):
    print(f"{index}: {NameList[index]}")
  print()


while True:
  firstName = input("What is your first name?: ").strip().capitalize()
  lastName = input("What is your last Name?: ").strip().capitalize()
  fullName = f"{firstName} {lastName}"
  if fullName not in NameList:
    NameList.append(fullName)
  displayName()
  
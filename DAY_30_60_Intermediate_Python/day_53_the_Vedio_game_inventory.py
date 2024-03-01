import os, time 

vedioInventory = []

try:
 file = open("VedioInventory.txt", "r")
 vedioInventory = eval(file.read())
 file.close()
except:
  print("We have a problem on our side, we will fix it soon")


def addItem():
  print("ADD")
  print()
  itemAdded = input("Add your item to the Inventory: ").capitalize()
  row = [itemAdded]
  vedioInventory.append(row)
  print(f"Your {itemAdded} has been added")
  time.sleep(2)
  os.system("clear")

def removeItem():
  print("You are removing an item")
  print()
  itemRemoved = input("What item do you want to remove: ").capitalize()
  if itemRemoved in vedioInventory:
      vedioInventory.remove(itemRemoved)
      print()
      print(f"Your item {itemRemoved} has been removed in the inventory")
  else:
    print("This item is not in the inventory")
  time.sleep(2)
  os.system("clear")

def viewItem():
  print("Viewing VedioInventor")
  itemViewed = input("""What do you want to view in the Inventory: 
        1: View all 
        2: View by count
        input your number: >>   """).capitalize()
  if itemViewed == "1":
   for row in vedioInventory:
      print(row)
   print()
  elif itemViewed == "2":
      seen = []
      for item in vedioInventory:
        if item not in seen:
         print(f"You have {item} {vedioInventory.count(item)}")
         seen.append(item)
  else:
    print("Invalid input")
  time.sleep(2)
  os.system("clear")

def editItem():
  print("What item you want to edit")
  itemEdited = input("What item do you want to edit: ").capitalize()
  found = False
  for row in vedioInventory:
    if itemEdited in row:
      found = True
  if not found:
      print("That item does not exist")
      return
  if row in vedioInventory:
      if itemEdited in row:
        itemEdited.remove(row)
        itemEdited = input("Input your new item: ").capitalize()
        row = [itemEdited]
        vedioInventory.append(row)
        print("Item has been edited")
  time.sleep(2)
  os.system("clear")
    

while True:
  print("Welcome to the Vedio Game Inventory")
  menu = input("""
        In the Vedio Invetory you can:
         1: Add
         2: View
         3: Remove
         4: Edit
         Characters frome the Vedio Games --
         your Input number: >>  """)
  if menu == "1":
    addItem()
  elif menu == "2":
    viewItem()
  elif menu == "3":
    removeItem()
  elif menu == "4":
    editItem()
  else:
    print("Invalid input")
  time.sleep(1)
  os.system("clear")


  file = open("VedioInventory.txt", "w")
  file.write(str(vedioInventory))
  file.close()

  
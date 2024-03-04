import os, time, random

print("Welcome to the ToDo list Management system")
print("-------------------------------------------")

myTodoList = []

fileExists = True
try:
  file = open("mytodo.txt", "r")
  myTodoList = eval(file.read())
  file.close()
except:
  fileExists = False




def preetyPrint():
  print()
  for row in myTodoList:
    for item in row:
      print(f"{item:^10}", end=" | ")
    print()
  print()

def addList():
  print("Add some thing to your list")
  print("+++++++++")
  activity = input("What is the activity? ")
  duration = input("How long will it take? ")
  day = input("What day is it due? " )
  priority = input("What is the priority? ")


  row = [activity, duration, day, priority]

  if row in myTodoList:
    print("This is already in the list")
  else:
    print("Added")
    myTodoList.append(row)

def viewList():
  print("View all your todolist or view by priority?")
  view = input("""
      1:view all
      2:view by priority 

      your input --- :  """)
  if view == "1":
   for row in myTodoList:
     for item in row:
       print(f"{item:^10}", end=" | ")
       print()
     print()
  else:
    priority = input("What priority? ")
    for row in myTodoList:
      if priority in row:
        for item in row:
          print(f"{item:^10}", end=" | ")
        print()
    print()


def editList():
   print("Edit your List?")
   search = input("What would you like to edit? ")
   found = False
   for row in myTodoList:
      if search in row:
        found = True
   if not found:
     print("Couldn't find that")
     return
   for row in myTodoList:
     if search in row:
        myTodoList.remove(row)
        activity = input("What is the activity? ")
        duration = input("How long will it take? ")
        day = input("What day is it due? " )
        priority = input("What is the priority? ")
        row = [activity, duration, day, priority]
        myTodoList.append(row)
        print("Edited")


def removeList():
  print("Remove from your list?")
  search = input("What would you like to remove? ")
  for row in myTodoList:
    if search in row:
      myTodoList.remove(row)
      print("Removed")




while True:
  menu = input("""What would you like to do?
       1:add
       2:view
       3:remove
       4:edit

       your input --- :  """)
  if menu == "add":
    addList()
  elif menu == "view":
    viewList()
  elif menu == "remove":
    removeList()
  elif menu == "edit": 
    editList()


  if fileExists:
    try:
      os.mkdir("backups")
    except:
      pass
      name = f"backup{random.randint(1,1000000000)}.txt"

      os.popen(f"cp mytodo.txt backups/{name}")


  file = open('mytodo.txt', 'w')
  file.write(str(myTodoList))
  file.close()





  preetyPrint()
  time.sleep(2)
  # os.system('clear')


# print(os.listdir())

# files = os.listdir()
# if 'my_good_file.txt' not in files:
#   print("Error: my_good_file.txt not found")

# os.mkdir("Welcome.txt")

# os.renames("Welcome.txt", "my_good_file.txt")

# filename = os.path.join("Hello/","some_good.txt")

# f = open(filename , "w")
# f.write("This is good")
# f.close()
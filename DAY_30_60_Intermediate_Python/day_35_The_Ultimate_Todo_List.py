import time, os 
myTodoList = []

def viewList():
   print('This are the activities you have this week')
   print()
   for index in range(len(myTodoList)):
     print(f"{index}: {myTodoList[index]}")
  

def editList():
  activity = input('What activity do you want to Edit?: ').title()
  new = input("Start editing it now? : ").title()
  for i in range(0, len(myTodoList)):
      if myTodoList[i] == activity:
        myTodoList[i] = new
        print(f"This is the new activity {new}")
  time.sleep(1)

def removeActivity():
   activity = input('What activity do you want to remove?: ')
   actions = input(f"Are you sure you want to remove {activity} from your list? ")
   if actions == 'yes':
     if activity in myTodoList:
         myTodoList.remove(activity)
   else:
         print('Okay, I will not remove it')
   time.sleep(1)



while True:
  print('This week Todo List Manager')
  actions = input("""Do you want to
                  1: view
                  2: add
                  3: edit
                  4: remove an activity from your todo list
                  5: delete
                  Input your action:  """ )
  if actions == 'view':
    viewList()
  elif actions == 'add':
    activity = input('What activity do you want to add?: ')
    myTodoList.append(activity)
  elif actions == 'edit':
     editList()
  elif actions == 'remove':
    removeActivity()
  elif actions == 'delete':
    myTodoList = [] 
  elif actions == '':
     print('Add something to the list First')


  time.sleep(1)
#   os.system("clear")
  

import random, os, time

print('The bingo random card numbers Generator')
print()

bingo = []

def generateRandomNumbers():
  num = random.randint(1,90)
  return num

def prettyPrint():
  for row in bingo:
   for item in row:
    print(f"{item:^10}", end=" | ")

def createCard():
  global bingo
  numbers = []
  for i in range(8):
    nums = generateRandomNumbers()
    while nums in numbers:
      nums = generateRandomNumbers()
    numbers.append(generateRandomNumbers())

  numbers.sort()

  bingo = [
    [numbers[0], numbers[1], numbers[2]],
    [numbers[3], "BINGO", numbers[4]],
    [numbers[5], numbers[6], numbers[7]]
]

createCard()
while True:
 prettyPrint()
 nums = int(input("Next Number: "))
 for row in range(3):
   for item in range(3):
     if bingo[row][item] == nums:
       bingo[row][item] = "X"



 exes = 0
 for row in bingo:
    for item in row:
      if item == "X":
        exes += 1

 if exes == 8:
    print("You have won")
    break

 time.sleep(1)
 os.system("clear")




# my2DList = []

# def prettyPrint():
#   print()
#   for row in my2DList:
#     for item in row:
#       print(f"{item:^10}", end=" | ")
#     print()
#   print()

# while True:
#   menu = input("Add or Remove? ")
  
#   if(menu.strip().lower()[0]=="a"):
    
#     name = input("What is your name? ")
#     age = input("What is your age? ")
#     language = input("Programming Language prefer? ")
    
#     row = [name, age, language]
#     my2DList.append(row)
    
#   else:
#     name = input("What name do you want to remove from the list")
#     for row in my2DList:
#      if name in row:
#       my2DList.remove(row)


#   prettyPrint()


# listOfShame = [] 

# while True: 
#   menu = input("Add or Remove?") 

#   if(menu.strip().lower()[0]=="a"): 

#     name = input("What is your name? ")
#     age = input("What is your age? ")
#     pref = input("What is your computer platform? ")

#     row = [name, age, pref] 

#     listOfShame.append(row) 


#   else: 
#     name = input("What is the name of the record to delete?") 
#     for row in listOfShame:
#      if name in row: 
#       listOfShame.remove(row) # remove the whole row if name is in it


#   print(listOfShame)
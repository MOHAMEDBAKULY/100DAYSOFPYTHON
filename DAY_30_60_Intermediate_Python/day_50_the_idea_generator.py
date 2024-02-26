import os, time, random
print("Welcome to the Idea Generator!")
user_name = input("What is your name? ")
print(f"Hello {user_name}! Karibu Hapa")
time.sleep(2)
os.system("clear")

def add_idea():
  file = open("my.ideas", "a+")
  userIdea = input("Write your Idea: ")
  file.write(f"{userIdea}\n")
  file.close()
  print("Your Idea has been added")
  time.sleep(2)
  os.system("clear")

def get_random_idea():
  file = open("my.ideas", "r")
  userIdeas = file.read().split("\n")
  file.close()
  if not userIdeas:
    print("No ideas matching idea was found")
    return
  userIdeas.remove("")
  random_Idea = random.choice(userIdeas)
  print("Your random idea is: ", random_Idea)
  time.sleep(2)
  os.system('clear')

while True:
  userInput = int(input("""
  With the idea Generator you can
        1: Add an idea
        2: Load a random idea
        3: Exit
        input your choice:    """))


  if userInput == 1:
    add_idea()
  elif userInput == 2:
    get_random_idea()
  elif userInput == 3:
    break
  else:
   print("Invalid input")
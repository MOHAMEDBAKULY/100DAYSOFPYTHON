import random, os, time
totalAttempts = 0

def game():
  attempts = 0
  while True:
    number = random.randint(1,100)
    guess = int(input("Pick a number between 1 and 100: "))
    if guess > number:
      print("Too high")
      attempts+=1
    elif guess < number:
      print("Too low")
      attempts+=1
    else:
      print("Just right!")
      print(f"{attempts} attempts this round")
      return attempts

while True:
  menu = input("1: Guess the random number game\n2: Total Score\n3: Exit\n> ")
  if menu == "1":
    totalAttempts+= game()
  elif menu == "2":
    print(f"You've had {totalAttempts} attempts")
  else:
    break







# for i in range(1,11):
#   print(i)

# import random

# colors = [ "red", "blue", "green","yellow", "purple", "orange",
#   "pink", "black", "white", "brown","gray","teal","navy",
#   "maroon","aqua","lime","olive","silver","gold","crimson",
#   "magenta", "cyan","fuchsia","indigo","violet","lavender",
#   "plum","tan","coral","peach","salmon","peru","sienna",
#   "chocolate","tan","burlywood","wheat","beige","cornflower",
#   "ivory","linen","olive","peach","salmon","sienna","slate",
#   "tan","thistle","tomato","violet","wheat","yellow"]

# while True:
#   menu = input("""
#        1:View colors
#        2:Get a random color
#        3:Exit
#        input your choice: """)

#   if menu == "1":
#     print(random.choice(colors))
#   elif menu == "2":
#     for color in colors:
#       print(color)
#   elif menu == "3":
#     break
    
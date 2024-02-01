#subroutine has parameter called `number`
#`number` shows how many numbers we want the pin to have
# def pinPicker(number):
#   import random
#   pin = "" #this is the empty string
#   for i in range(number): #for loop shows defined amount of random numbers
#     pin += str(random.randint(0,9)) #we want a string of random numbers between 0-9
#   return pin

# myPin = pinPicker(6)#4 means we want 4 random number
# print(myPin)

# def areaOfTriangle(base, height):
#   area = 0.5 * base * height
#   return area

# myAnswer = areaOfTriangle(5, 22)

# print(myAnswer)
red = '/033[31m';
yellow = '/033[33m';
reset = '/033[0m';

import random
print("""CHARACTER STAT GENERATOR
         WELCOME TO THE GAME
""")
user_name = input("What is your name? ")
print('Hello', user_name,'!')

def roll_dice(sides):
  result = random.randint(1,sides)
  return result

def roll_6_and_8():
  roll_6_sided_dice = roll_dice(6)
  roll_8_sided_dice = roll_dice(8)
  health = roll_6_sided_dice * roll_8_sided_dice
  return health


have_a_character = "yes"

while have_a_character == 'yes':
  character = input("Give your character a name: ")
  health = str(roll_6_and_8())
  print(user_name,'your character is called',character,'has', health, 'health points')
  have_a_character = input("Want to create another character? ")
  continue
  if have_a_character == 'no':
    print(user_name, 'thank you for playing!')
    break
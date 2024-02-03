import time, os, random
  
def roll_dice(sides):
  result = random.randint(1,sides)
  return result

def health():
  health_stat = ((roll_dice(6)*roll_dice(12))/2)+10
  return health_stat

def strength():
  strenght_stat = ((roll_dice(6)*roll_dice(12))/2)+12
  return strenght_stat

while True:
  print('Welcome to the character generator')
  your_name = input('What is your name:? ')
  print('Hello', your_name)
  print()

  def genarate_character(first_name, type):
    if type == "human" or type == "elf" or type == "wizard" or type == "orc":
      print('You have picked', type , 'as your character type')
      if first_name == "":
        print('You have picked', first_name , 'as your character name')
        return first_name + " the " + type

  the_name = input('What is the name of your character:? ')
  the_type = input('What is the type of your character:? ')

  genarate_character(the_name, the_type)
  print('Health:', health())
  print('Strenght:', strength())
  print()
  print('May your name go down in Legend...')
  print()
  again = input('Would you like to create another character?: ')
  if again == 'No' or again == 'no':
   break
time.sleep(1)  
os.system('clear')
  
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



print('Welcome to the character generator')
your_name = input('What is your name:? ')
print('Hello', your_name)
print()

c1Name = input('What is the name of your character:? ')
c1type = input('Character type (Human, Elf, Wizard, Orc):? ')
print()
print(c1Name,'is the name of your character')
print(c1type,'is the type of your character')
c1Health = health()
c1Strenth = strength()
print('Health:', c1Health)
print('Strenght:', c1Strenth)
print()
print('Who are you ready to fight today?')

c2Name = input('What is the name of your character:? ')
c2type = input('Character type (Human, Elf, Wizard, Orc):? ')
print()
print(c2Name,'is the name of your character')
print(c2type,'is the type of your character')
c2Health = health()
c2Strenth = strength()
print('Health:', c2Health)
print('Strenght:', c2Strenth)
print()

round = 1
winner = None

while True:
  time.sleep(1)  
  os.system('clear')
  print('Welcome to the character Battle')
  print()
  print('let the battle begins')
  print()

  c1Dice = roll_dice(6)
  c2Dice = roll_dice(6)

  difference = abs(c1Strenth - c2Strenth) + 1

  if c1Dice > c2Dice:
    c2Health -= difference
    if round == 1:
      print(c1Name, 'wins the first blow')
    else:
      print(c1Name, 'wins round', round)
  elif c2Dice > c1Dice:
    c1Health -= difference
    if round == 1:
      print(c2Name, 'wins the first blow')
    else:
      print(c2Name, 'wins round', round)
  else:
    print('Their swords clash and they draw round', round)

    print()
    print(c1Name)
    print('Health:', c1Health) 
    print()
    print(c2Name)
    print('Health:', c2Health)
    print()


    if c1Health <= 0:
      print(c1Name, 'has died!')
      winner = c2Name
      break
    elif c2Health <= 0:
      print(c2Name, 'has died!')
      winner = c1Name
      break
    else:
      print('Continue fighting guys')
      round += 1

time.sleep(1)
os.system('clear')
print('Welcome to the character Battle')
print()
print(winner, 'has won in', round, 'rounds')
print(your_name,'Thank you for particpating in the Battle')

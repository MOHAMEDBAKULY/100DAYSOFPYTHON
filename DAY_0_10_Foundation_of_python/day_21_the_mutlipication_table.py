red = "\033[31m"
green = "\033[32m"
reset = "\033[0m"

print("""Welcome to the Math Game
       where you will be learning more about 
       multiplication tables
""")
name = input("What is your name? ")
print('Hellowoo',green, name, reset, 'Welcome to the Math Game')
print(name, 'you will be only multiplying a number upto 10')
choosed_number = int(input("Choose a number and workout it's correct Multiples : "))
print('You have chosen the number', red, choosed_number, reset)
print()
print()
print('Lets start the game')
points = 0

for i in range(1, 11):
  correct_answer = choosed_number * i
  print(i, 'x', choosed_number)
  answer = int(input('> '))
  if answer == correct_answer:
    print(green, 'Great work!', reset)
    points += 1
  else:
    print(red, 'Nope. The answer was', correct_answer, reset)

  
  if  points == 10:
    print('Perfect', name, 'You scored', green, points, reset, 'out of 10')
  else:
    print(name,'You scored', green, points, reset, 'out of 10')


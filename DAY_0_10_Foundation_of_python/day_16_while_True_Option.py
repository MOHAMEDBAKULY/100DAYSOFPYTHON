print('Who is the best footballer in the world')
print('You can do a Google search or you can try to answer')
print()
attempts = 0

while True:
  name = input('Who is the best footballer in the world?: ')
  ballon_dor = int( input('How many ballon dor does he have?:'))
  attempts += 1
  if name == 'Messi' and ballon_dor == 8:
    print('You are right')
    break
  else:
    print('You are wrong')
    print('You had', attempts, 'attempts to get is right')

# while True:
#   print("This program is running")
# print("Aww, I was having a good time 😭")


# while True:
#   print("This program is running")
#   goAgain = input("Go again?: ")
#   if goAgain == "no":
#     break
# print("Aww, I was having a good time 😭")


# while True:
#   print('Welcome to the whil loop breaker excercise')
#   Your_Age = int(input('How Old are you?: '))
#   print('Keep Pushing my G you still have gase')
#   stop_loop = input('Do you want to stop the loop?: ')
#   if stop_loop == 'yes':
#     break
# print('It was nice taliking to you')

# counter = 0;
# while True:
#   answer = int(input('What is the date today?: '))
#   print('It should be greater than the last date')
#   counter += answer 
#   print('Current Total is', counter)
#   add_another = input('Do you want to add another?: ')
#   if add_another == 'no':
#     break
# print('Have a nice day')


# while True:
#   color = input("Enter a color: ")
#   if color == "red":
#    break
#   else:
#     print("Cool color!")
# print("I don't like red")


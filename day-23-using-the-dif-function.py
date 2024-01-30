# def date_today():
#   import random
#   day = random.randint(1,31);
#   print('What is the date today?', day)

# for i in range(10):
#   date_today()

# def print_favorite_color():
#  print("My favorite color is red.")
#  name = input("What is your name?")
#  print(name, 'Welcome to using Subroutines or Functions or defenitions in Python')

# print_favorite_color()
green = '\033[32m'
red = '\033[31m'
reset = '\033[0m'

print('Welcome to Replit 100 days of code')
print('This is a login system')

def User_Login():
 while True:
   user_name = input('What is your name:? ')
   password = input('What is your password:? ')
   if user_name == 'Bakuly' and password == '100daysOfCode':
     print('Welcome to Replit')
     print(red,user_name,reset, 'Welcome to Replit and  your password is',green,password,reset,)
     break
   else:
     print('Whoops! I don\'t recognize that username or password. Try again!')
     

User_Login()
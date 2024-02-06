# name = "Bakuly"
# age = "24"
# pronouns = "he/him"
# religion = "Islam"

# print("This is", name, "using", pronouns, "pronouns and is", age, "years also is a", religion)

# name = "Mohamed"
# age = "24"
# pronouns = "he/him"
# religion = "Islam"

# print("This is {}, using {} pronouns, and is {} years old practising Islam".format(name, pronouns, age, religion))

# name = "Mohamed"
# age = "24"
# pronouns = "he/him"
# religion = "Islam"

# print("This is {name}, using {pronouns} pronouns, and is {age} years old, practising {religion}. Hello, {name}. How are you? Have you been having a great {age} years so far".format(name=name, pronouns=pronouns, age=age, religion=religion))

# name = "Mohamed"
# age = "24"
# pronouns = "he/him"
# religion = "Islam"
# sports = "Martial Arts"

# response = "This is {name}, using {pronouns} pronouns, and is {age} years old, his sport is {sports}.How are you? {name} How does it feel to be at {age} years so far,how is {religion} now".format(name=name, pronouns=pronouns, age=age, religion=religion, sports=sports)

# print(response)

# name = "Mohamed"
# age = "24"
# pronouns = "he/him"
# religion = "Islam"
# sports = "Martial Arts"

# response = f"""This is {name}, using {pronouns} pronouns, and is {age} years old, his sport is {sports}.

# How are you? {name} How does it feel to be at {age} years so far,how is {religion} now"""

# print(response)

# red = "\033[31m"
# blue = "\033[34m"
# green = "\033[32m"
# reset = "\033[0m"
# for i in range(1, 31):
#   if i <= 10:
#     print(f"{red}Early days {i: >3} of 100 days of code{reset}")
#   elif i > 10 and i <= 20:
#     print(f"{green}Middle days {i: >3} of 100 days of code{reset}")
#   else:
#     print(f"{blue}Late days {i: >3} of 100 days of code{reset}")

# food = "pizza"
# location = "beach"
# color = "green"
# friend = "Quinn"

# response = f"""Alejandra ordered {food} to eat at the {location} with her friend, {friend}. 

# She got to the {location} and looked for a {color} umbrella where {friend} said they would be waiting. By the time, Sally found {friend}, the {food} was cold and the {location} was lame."""

# print(response)
import time, os

print('Welcome, To the Python 30 days Quiz:')
print()
user_name = input('What is your name? ')
print()
print(f"Hello,{user_name} welcome to the survey of 30 days of Python")
print()
time.sleep(1)
os.system('clear')
yellow = "\033[33m"
blue = "\033[34m"
purple = "\033[35m"
reset = "\033[0m"

for quiz in range(1,31):
  if quiz <= 10:
    print(f"{yellow} Day {quiz: ^3} of 30{reset}")
    print()
  elif quiz > 10 and quiz <= 20:
    print(f"{blue} Day {quiz: >2} of 30{reset}")
    print()
  else:
    print(f"{purple} Day {quiz: >2} ")
  print(f"Day {quiz: >2} of 30 days of code")
  print()
  user_opinion = input(f'How was your experience in day {quiz}:?  ')
  print(f"{user_name} You thought Day {quiz} was {user_opinion}")
  print()
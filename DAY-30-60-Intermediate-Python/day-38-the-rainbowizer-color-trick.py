# vowels = ['a', 'e', 'i', 'o', 'u']

# type_something = input("Type your favorite sentence: ")
# for letter in type_something:
#   if letter.lower() in vowels:
#     print('\033[34m', end='')
#   print(letter)
#   print('\033[0m', end='')

def colorChange(color):
   if color == "r":
    print("\033[31m", end="")
   elif color == "b":
    print("\033[34m", end="")
   elif color == " ":
    print("\033[0m", end="")
   elif color == "y":
    print("\033[33m", end="")
   elif color == "g":
    print("\033[32m", end="")
   elif color == "p":
    print("\033[35m", end="")
   elif color == "c":
    print("\033[36m", end="")
    

print('Welcome to the rainbowizer!')
user_name = input('What is your name? ')
print()
print(f"Hello {user_name}!👋 welcome")
print()

for name in user_name:
  colorChange(name.lower())
  print(name, end="")
print()

user_input = input('Type any sentence your like: ')
for latter in user_input:
  colorChange(latter.lower())
  print(latter, end="")
  print()

print(f"""{user_name},
Thank you for using the rainbowizer!
this was your sentence {user_input}
""")
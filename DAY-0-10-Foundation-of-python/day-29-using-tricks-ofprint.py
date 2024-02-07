# for i in range(0, 100):
#   print(i, end=" Hi ")

# print("If you put")
# print("\033[33m", end="") #yellow
# print("nothing as the")
# print("\033[35m", end="") #purple
# print("end character")
# print("\033[32m", end="") #green
# print("then you don't")
# print("\033[0m", end="") #default
# print("get odd gaps")

# print('Random green car passing by', "\033[32m",
#      'The car is green', "\033[33m", 'and is driving slowly ', sep="woow")

# print("If you put ", "\033[33m", "nothing as the ", "\033[35m", "end character ", "\033[32m", "then you don't ", "\033[0m", "get odd gaps ", sep="")

# import os, time
# print('\033[?25l', end="")
# print('\033[?25h', end="")')
# for i in range(1, 101):
#   print(i)
#   time.sleep(0.3)
#   os.system("clear")



print('Welcome to the Color printing game')
your_name = input('What is your name? ')
print('Hello', your_name, 'let the game begin')

def word_color(word, color):
  if color == 'red':
    print('\033[31m', word, sep="", end="")
  elif color == 'green':
    print('\033[32m', word, sep="", end="")
  elif color == 'blue':
    print('\033[34m', word, sep="", end="")
  elif color == 'yellow':
    print('\033[33m', word, sep="", end="")
  elif color == 'purple':
    print('\033[35m', word, sep="", end="")
  elif color == 'white':
    print('\033[37m', word, sep="", end="")
  else:
    print('\033[0m', word, sep="", end="")


user_word = input('What word do you want to print? ')
user_color = input('What color do you want to print? ')
print()
print('This is the word you chose', user_word, 'and here is the color you gave it', user_color,)
print()
word_color(user_word, user_color)
print()
print(your_name, 'you are amazing, with the choice of your colors.')
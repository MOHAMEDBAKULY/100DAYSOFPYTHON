# for numbers in range(20, 30):
  # print(numbers)

# for days in range(1, 8):
#    print("Day", days)

# print("Thirteen Times Table")
# for i in range(1, 13):
#   print(i, "x 13 =", i * 13)

# print('one to 50 by 5 increments')
# for number in range(0, 51, 5):
#   print(number, '* 5 =', number * 5)

# print('Counting Backwards from 51 to 0')
# for number in range(51, 0, -5):
#   print(number)

# for i in range (10, 20):
#   print(i)

# for i in range(20, 40, 1):
#   print(i)

green = "\033[0;32m"
yellow = "\033[0;33m"
red = "\033[0;31m"
reset = "\033[0m"

print('Welcome to the number counter')
your_name = input('What is your name:? ')
print('Welcome the number counter', green, your_name,'!', reset)
start_numb = int(input('What number would you like to start at? '))
print('Okay, starting at', green, start_numb, reset)
end_numb = int(input('What number would you like to end at? '))
print("Okay, ending at", green, end_numb, reset)
increments = int(input('What increments would you like to count by? '))

print()

for i in range(start_numb, end_numb, increments):
  print(i)

print('Thank you for using the number counter', your_name, '!')
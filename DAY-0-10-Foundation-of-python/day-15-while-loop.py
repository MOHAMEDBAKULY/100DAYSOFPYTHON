exit = ''
while exit != 'yes':
  in_three_months = input("What do you want to acheive in the next 3 months?: ")
  if in_three_months == 'Postman-lead':
    print('That is acheiveable if you put in the work')
    exit = input("Do you want to give up?: ")
    something_else = input("What else do you want to acheive in the next 3 months?: ")
    if something_else == 'Yellow-Belt':
      print('That is  also acheiveable if you put in the work and time')
      exit = input("Do you want to give up?: ")
      print('Thank you for being Honest with your self')


# You can uncomment this to run the code
# counter = 0
# while counter < 20:
#   print("This is ", counter)
#   counter +=1

# You can also use a for loop to iterate over a list
# exit = ""
# while exit != "yes":
#   print("🥳")
#   exit = input("Exit?: ")


  
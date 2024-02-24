print("How to know which career is best for you?: ")
print("Welcome to the game 🗺️ ___")
print("You will be asked a series of questions to find out which career is best for you!")
print("Please answer the questions with the number that corresponds to your answer.")
print("Let's begin!")
# Question 1
print("Question 1: What is your favorite hobby?")
hobby = input(" What do you do in your free time? ")
# Question 2
print("Question 2: What is grade?")
grades = input("What was your passmark in your last exam?")
# Question 3
print("Question 3: What is your favorite subject?")
subject = input("What is your favorite subject?")

if hobby == "Drawing":
  print("You are artistic in nature consider art degrees")
elif hobby == "Reading":
  print("You should do philosophy or psychology")
if grades >= "90":
          print("You should do a master degree in psychology")
elif grades == "70":
          print("You should do a master degree in philosophy")
else:
    print("You should do a master degree in {subject}")
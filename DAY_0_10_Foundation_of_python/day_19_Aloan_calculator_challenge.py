blue = "\033[94m"
green = "\033[93m"
reset = "\033[0m"

print("The Loan Calculator Challange")
your_name = input('What is your name:? ')
print("Hello", your_name)
loan_amount = int(input("How much do you want to borrow?: "))
print("You want to borrow", loan_amount, "dollars")
loan_duartion = int(input("For how long?: "))

annul_principal_return = 0.05
total_interest_paid = 0
for year in range(loan_duartion):
  interest = (loan_amount * annul_principal_return)
  loan_amount += interest
  total_interest_paid += interest
  print(your_name,"in Year", year + 1, "your loan is", round(loan_amount, 2))
  print(blue, your_name, 'You paid', round(interest, 2), 'dollars in interest in year', year + 1, reset)
  print(green, your_name, 'Total interest paid over', loan_duartion, 'years:', round(total_interest_paid, 2), reset)


# counter = 0
# while counter < 10:
#   print(counter)
#   counter += 1

# total = 0
# for counter in range(10):
#   total += counter
#   # print(total)

# for days in range(7):
#   print("Day", days + 1)


# Colors of the amnount

  
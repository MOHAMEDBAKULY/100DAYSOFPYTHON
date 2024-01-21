print("Tip calculator: ")
totalBill = float(input("What was the cost of the meal:? "))
tipPercent = float(input("What percent tip would you like to leave? "))
numPeople = int(input("How many people are splitting the bill? "))
tipAmount = totalBill * (tipPercent / 100)
totalAmount = totalBill + tipAmount
amountPerPerson = totalAmount / numPeople
roundedBill = round(amountPerPerson, 2)
print("The total tip amount is: ", tipAmount)
print("The total amount is: ", totalAmount)
print("The amount per person is: ", amountPerPerson)
print("The rounded amount per person is: ", roundedBill)
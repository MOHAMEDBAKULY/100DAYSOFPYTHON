import csv

try:
 with open("Day54Totals.csv") as file:
  reader = csv.DictReader(file)
  cost = 0
  quantity = 0
  for row in reader:
    # print("\t ,".join(row))
    print(row["Cost"], row["Quantity"])
    cost += float(row["Cost"])
    quantity += float(row["Quantity"])
 print(f"Items cost: {cost}")
 print(f"Quatity of item: {quantity}")
 print(f"Your shop took KES{round(cost * quantity, 2)} as sales today")
except:
  print("You don't have a file named Day54Totals.csv")


# import csv # Imports the csv library

# with open("January.csv") as file: 
#   reader = csv.DictReader(file) 
#   line = 0
#   total = 0
#   for row in reader: 
#     print (row["Net Total"])
#     total += float(row["Net Total"])

# print(f"Total: {total}")

# import csv # Imports the csv library

# with open("January.csv") as file: 
#   reader = csv.DictReader(file) 
#   line = 0
#   total = 0
#   for row in reader: 
#     print (row["Expenditure"])
#     total += float(row["Expenditure"]) 

# print(f"Expenditure: {total}")

# import csv

# with open("January.csv") as file:
#   reader = csv.DictReader(file)
#   line = 0
#   for row in reader:
#     print(row["Net Total"])

# import csv # Imports the csv library

# with open("January.csv") as file:  # Open the CSV FILE
#   reader = csv.DictReader(file) # Treats the file as a dictionary 
#   total = 0
#   for row in reader: 
#     # print("\t ".join(row))
    # print("\t  ".join(row))
#     # print (row["Net Total"])
#     print(row["Expenditure"])
#     total += float(row["Expenditure"]) # Keeps a running total

# print(f"Expenditure: {total}") #Outputs
    
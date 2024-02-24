print("Welcome to the String Manipulation tricks")
while True:
 fname = input("What is your first name? ").upper()
  
 lname = input("What is your last name? ").upper()
 print(f"Hello {fname} {lname}")
 father_name = input("What is your father's first name? ").lower()
 village_name = input('What is the name of the village he was born? ').upper()
 print(f"Your father's name is {father_name} and he was born at {village_name}")
 print()
 print(f""" This is your Star wars name
      {fname[0:3]}{lname[:3]} {father_name[:2]}{village_name[:3]}
  """)
 break





# assignment = ("In the next Two weeks we will be learning about Python Programming").upper()
# manipulation = (assignment.split()[0: 8: 2])

# for index in range(len(manipulation)):
#   print(f"This is word {index} of the list {manipulation[index]}")

# This code should output 'Hello there
# myString = ("Hello there my friend.").lower()
# print(myString.split()[0:15:1])
# tString data types


#Literal string assingment

firstName = "Mohamed"
lastName = "Bakuly"

# print(type(firstName))
# print(type(firstName) == str)
# print(isinstance(firstName, str))
# print(f"{firstName} {lastName}")

# armani = str("White Milk")
# print(type(armani))
# print(type(armani) == str)
# print(isinstance(armani, str))
# print("Build your startUp") if entryAge > 20 else print("Build up your skills first")

# myName = firstName + " " + lastName + " "
# myName += "wow"
# print(myName)

#Casting a number to a string
# cast = str(2024)
# print(type(cast))

# activity = "Today i did not go to training on" + cast + ".saturday"
# print(activity)
# print(activity.upper())
# print(activity.lower())
# print(activity.title())
# print(activity.capitalize())
# print(activity.replace("Today", "Earlier Today"))
# print()

multiline = """"
  How Fun is it to use Python?
          It's a simple powerful language
             and gives you alot of skills 
"""

print(len(multiline))
multiline += "      "
multiline = " hapa ndio inabamba " + multiline
print(len(multiline))
print(multiline)
print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))
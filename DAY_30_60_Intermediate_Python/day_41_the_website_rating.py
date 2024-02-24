print("Welcome to the Website info generator")

website_info = {
  "Name": None,
  "URL": None,
  "Description": None,
  "Rating":None
}


for name,value in website_info.items():
  website_info[name] = input(f"{name} : ")
  
print()
for name, value in website_info.items():
  print(f"{name} : {value}")


# six_months = {
#   "January": "Finalishing Javascript",
#   "February": "Making 6 full design case studies",
#   "March": "Starting MySQL",
#   "April": "Building Projects with Python",
#   "May": "Starting off the building of PhotoHive",
#   "June": "Becoming a Founder of a Startup",
#   "days": 29
# }

# for i in six_months:
#   print(six_months[i])

# for value in six_months.values():
#   print(value)

# for name, value in six_months.items():
#   print(f"{name}: {value}")
#   if name == "days":
#     if value >= 30:
#      print("I'm in May!")
#     else:
#       print("I'm not in May!")

# for name, value in six_months.items():
#   print(f"{name}: {value}")
#   print()
#   if name == "February":
#     print('Try hard this month and make things happen')
#   print()


# myDictionary = {"name" : "Ian", "health": 219, "strength": 199, "equipped": "Axe"}

# for name, value in myDictionary.items():
#   print(f"{name}: {value}")
#   if name == "health":
#     print('I need to drink more water')
#     if value >= 100:
#       print("I'm in good shape!")
#     else: 
#       print("I need to exercise more")
# myDictionary = {"name" : "David the Mildy Terrifying", "health": 186, "strength": 4, "equipped":"l33t haxx0r p0werz"}

# for name, value in myDictionary.items():
#   print(f"{name}:{value}")
#   if name == "strength":
#     if value > 100:
#      print("Whoa, SO STRONG")
#   else:
#     print("Looks like you skipped leg day, arm day, chest day and, well, gym day entirely bro!")


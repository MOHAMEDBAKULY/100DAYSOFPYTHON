print("Welocome to the Moke Beast Character Creator")
print()
print("Beast type should be Earth, Fire, Air, Water or Spirit to have color display")
print()

the_Moke_Beast = {}

for name, value in the_Moke_Beast.items():
  the_Moke_Beast[name] = input(f"{name}: ").strip().title()

for name, value in the_Moke_Beast.items():
  print(f"{name: <10}: {value}")



def preetyPrint():
  for key,value in the_Moke_Beast.items():
    print(key, end=": ")
    for subkey, subvalue in value.items():
      print(subkey, subvalue, end=" | ")
    print()




while True:
  name = input("Beast Name: ")
  type = input("Beast Type: ")
  specialMove = input("Beast Special Move: ")
  startingHP = int(input("Beast Starting HP: "))
  startingMP = int(input("Beast Starting MP: "))
  the_Moke_Beast[name] = {"type": type, "specialMove": specialMove, "startingHP": startingHP, "startingMP": startingMP}
  preetyPrint()

# for type, value in the_Moke_Beast.items():
#   if the_Moke_Beast["type"] == "Earth":
#     print("\033[31m", end="")
#   elif the_Moke_Beast["type"] == "Air":
#     print("\033[37m", end="")
#   elif the_Moke_Beast["type"] == "Fire":
#     print("\033[31m", end="")
#   elif the_Moke_Beast["type"] == "Water":
#     print("\033[34m", end="")
#   else:
#     print("\033[33m", end=""
  
# institutions = {}

# def preetyPrint(key, value):
#   print()
#   for key, value in institutions.items():
#     print(key, end=": ")
#     for subKey, subValue in value.items():
#       print(subKey, subValue, end=" | ")
#     print()
  
# while True:
#   name = input("Institution name: ")
#   location = input("Institution location: ")
#   type = input("Institution type: ")
#   started = input("Institution started: ")
#   institutions[name] = {"location": location, "type": type, 
#   "started": started}

#   preetyPrint()
print("Welocome to the Moke Beast Character Creator")
print()

the_Moke_Beast = {
  "name": None,
  "type": None,
  "special move": None,
  "starting HP": None,
  "starting MP": None
}

for name, value in the_Moke_Beast.items():
  the_Moke_Beast[name] = input(f"{name}: ").strip().title()

if the_Moke_Beast["type"] == "Earth":
  print("\033[31m", end="")
elif the_Moke_Beast["type"] == "Air":
  print("\033[37m", end="")
elif the_Moke_Beast["type"] == "Fire":
  print("\033[31m", end="")
elif the_Moke_Beast["type"] == "Water":
  print("\033[34m", end="")
else:
  print("\033[33m", end="")


for name, value in the_Moke_Beast.items():
  print(f"{name: <10}: {value}")

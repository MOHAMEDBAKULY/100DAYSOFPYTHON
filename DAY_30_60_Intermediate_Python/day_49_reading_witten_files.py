print("Current Leader Score board")
print()
file = open("fileNames.list", "r")
getWinner = file.read().split("\n")
file.close()


highscorer = 0
name = None

for rows in getWinner:
  data = rows.split()
  print(data)
  if data != []:
    if int(data[1]) > highscorer:
      highscorer = int(data[1])
      name = data[0]
  
print("The winner is", name, "with", highscorer)




# file = open("fileNames.list", "r")
# while True:
#   contents = file.readline().strip()

#   if contents == "":
#     break

#   print(contents)

# file.close()
# while True:
#   file =  open("fileNames.list", "a+")
#   initials = input("Input your initial:  ").upper()
#   file.write(f"{initials}")
#   score = int(input("Input any 5 digits number: "))
#   file.write(f" {score}\n")
#   inputFiles = input("Want to add more files (yes/no)?  ")
#   if inputFiles == "yes":
#    continue
#   elif inputFiles == "no":
#    break
# file.close()
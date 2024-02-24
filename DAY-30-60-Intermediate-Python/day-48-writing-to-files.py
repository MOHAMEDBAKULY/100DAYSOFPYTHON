print("Welcome to the High-Score Program")


while True:
  print()
  sFile = open("high.score.txt", "a+")
  initials = input("> Input your initials just 3 letters:  ").upper()
  sFile.write(f"{initials}")
  score = int(input("> Input your score around 6 digits:  "))
  sFile.write(f"  {score}\n")
  sFile.close()
  exit = input("Do you want to exit? (y/n)  ")
  if exit == "n":
    print("Okay, let\'s continue")
    continue
  elif exit == "y":
    print("Okay, bye!")
    break
  else:
    print("I don't understand, bye!")
    break




# secondPythonFile = open("python_file.txt", "a+");
# userInput = input("Write Something: ");
# secondPythonFile.write(f"{userInput}\n");
# userInput = input("Write Something else: ");
# secondPythonFile.write(f"{userInput}\n");
# secondPythonFile.close();


# f = open("savedFoal.txt", "a+")
# whatText = input("> First Input: ")
# f.write(f"{whatText}\n")
# whatText = input("> Second Input: ")
# f.write(f"{whatText}\n")
# f.close()


# secondPythonFile = open("python_file.txt", "w");
# secondPythonFile.write("This is my second python file" + "\n");
# userInput = input("Write Something: ");
# secondPythonFile.write(userInput);
# secondPythonFile.close();



# firstPythonFile = open("my_python_file.txt", "w")
# firstPythonFile.write("This is my first python file!")
# print()
# firstPythonFile.write("How to write to a file in Python!")
# print()
# firstPythonFile.write("Open a connection using the .open() Command!")
# print()
# firstPythonFile.write("You need to have a file path ending with File.txt to")
# print()
# firstPythonFile.write("The w means you are writing to a file if it's not there and also overwrite the content if it was created")
# print()
# firstPythonFile.write("The .write() command is used to write to a file")
# print()
# firstPythonFile.write("The .close() command is used to save the File")
# firstPythonFile.close()
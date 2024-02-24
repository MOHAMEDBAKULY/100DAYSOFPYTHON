print("""Welcome to my Day 8 Challenge
     I have a series or questions for 
          you to answer.
      be open and 💖honest."""
 )
print("Be ready to know your future car")
print()
userName = input("What is your name? ")
userAge = input("How old are you? ")
userGender = input("What is your gender? ")
drivingExperince = input("How many years of driving experince do you have? ")
print()
car = input("What is your favorite car brand? ")
if car == "audi" :
  print("You are a lucky person");
  carModel = input("What is your favorite car model? ")
  if carModel == "A3" or carModel == "S3":
    print('You are addicted to Audi')
    speedLimit = input("What is the speed limit in your area? ")
    if speedLimit == "230" or speedLimit == "100":
     print('Speed kills be careful while driving')
elif car == "bmw" :
  print('German car is the best')
  carModel = input("What is your favorite car model? ")
  if carModel == "M3" or carModel == "M5":
    print('You are addicted to BMW')
    speedLimit = input("What is the speed limit in your area? ")
    if speedLimit == "230" or speedLimit == "100":
      print("speed Kills be careful while driving")
else:
  print("You are not a car person")
print()
print("Hello", userName, "you are", userAge, "years old", "and you are a", userGender, "and you have", drivingExperince, "years of driving experince", "and your favorite car is", car, "What model of audi or bmw you like", carModel, "and the speed limit in your area is", speedLimit, "Thank you for your time")
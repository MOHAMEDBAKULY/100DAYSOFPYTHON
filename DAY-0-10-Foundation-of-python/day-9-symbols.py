print("The questions that follow will evaluate which generation you are a part of.")
print("Please input the year your correctly to get honest feedback.")
print(" ")

yearBorn = int(input("Input the year you were born:" ))
if yearBorn >= 1925 and yearBorn <= 1946 :
  print("You are a Traditionalist.")
elif yearBorn >= 1947 and yearBorn <= 1964 :
  print("You are a Baby Boomer.")
elif yearBorn >= 1965 and yearBorn <= 1981 :
  print("You are a Generation X.")
elif yearBorn >= 1982 and yearBorn <= 1995 :
  print("You are a Millenial.")
elif yearBorn >= 1996 and yearBorn <= 2015 :
  print("You are a Generation Z.")
else:
  print("You are a Generation Alpha.")
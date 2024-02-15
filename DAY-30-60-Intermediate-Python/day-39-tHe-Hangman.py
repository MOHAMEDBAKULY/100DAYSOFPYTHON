import random, os , time

red = "\033[0;31m"
green = "\033[0;32m"  
yellow = "\033[0;33m"
reset = "\033[0m"
# List of countries 
east_african_countries = ['Kenya', 'Uganda', 'Tanzania', 'Rwanda', 'Burundi', 'South Sudan', 'Sudan', 'Ethiopia', 'Djibouti', 'Eritrea', 'Somalia','Congo']
# Knowing the user's name
user_name = input("What is your name? ")
print()
print(f""" {green}Welcome {user_name} to the hangman game!{reset}
  {yellow}You have to guess the name of the countries in East African Region:{reset} """)
print()
# Randomly choosing a country from the list
random_country = random.choice(east_african_countries)
guessed_letters = []
attempts = 6

while True:
  time.sleep(2)
  os.system("clear")
  choosed_letter = input(f'Type your guessed letter {user_name}: ').capitalize()
  
  if choosed_letter in guessed_letters:
    print("You already picked this letter")
    continue
    
  guessed_letters.append(choosed_letter)

  
  if choosed_letter in random_country:
    print("You have guessed a correct letter")
  else:
    print("You have guessed a wrong letter")
    attempts -= 1

  right_letters = True
  print()
  for letter in random_country:
      if letter in guessed_letters:
        print(letter, end="")
      else:
        print("_", end = "")
        right_letters = False
  print()

  if right_letters:
    print(f"Congragulations you have won with {attempts} attempts left")
    break

  if attempts <= 0:
   print(f"You have no attempts left! the right coutnry was {random_country}")
   break
  else:
   print(f"You have {attempts} attempts left")
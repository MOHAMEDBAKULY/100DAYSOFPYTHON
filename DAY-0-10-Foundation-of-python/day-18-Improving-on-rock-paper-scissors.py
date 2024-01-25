print("""Guess the Number Game
      Welcome to the Guess the Number Game!
""")
print('The number should be between 1 and 1000000')


number = 290
trials = 0

while True:
  your_name = input("What is your name? ")
  print(f"Hello {your_name}! Welcome to the Guess the Number Game!")
  guess_number = int(input("What is your guessed number: "))
  
  if guess_number == number:
   print(your_name, 'You have read my mind', guess_number, 'is the correct number after', trials, 'trials' )
   trials += 1
   exit()
  elif guess_number < 1:
   print('No negative numbers', your_name)
   trials += 1
  elif guess_number > 1000000:
   print('No numbers above 1000000', your_name)
   trials += 1
  elif guess_number == number:
    print(your_name, 'You have read my mind', guess_number, 'is the correct number' )
    trials += 1
    break
  elif guess_number >= 200 and guess_number <= 1000:
    print(your_name, 'You are too close, you chose', guess_number)
    trials += 1
  elif guess_number >= 10000 and guess_number <= 100000:
    print(your_name, 'You are a little bit high, you chose', guess_number )
    trials += 1
  elif guess_number >= 200000 and guess_number <= 500000:
    print(your_name, 'You are very far from being right, you chose', guess_number)
    trials += 1
  elif guess_number >= 600000 and guess_number <= 1000000:
    print(your_name, 'that is peek guess lower, you chose', guess_number)
    trials += 1
    continue

    
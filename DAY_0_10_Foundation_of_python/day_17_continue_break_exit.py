from getpass import getpass as input

print()
print('Let the game begin!')

print()
players_attempts = 0
player1_score = 0
player2_score = 0
print()

while True:
  player1_name = input('Player 1, please enter your name: ')
  print('Welcome to the game', player1_name)
  player2_name = input('Player 2, please enter your name: ')
  print('Welcome to the game', player2_name)

  player1_choice = input(player1_name + ' please choose R, P, or S: ')
  print()
  player2_choice = input(player2_name + ' please choose R, P, or S: ')
  print()

  if player1_choice == 'R':
   if player2_choice == 'R':
    print('It is a tie!', player1_name, 'and', player2_name, 'both chose Rock!')
   elif player2_choice == 'P':
    print(player2_name, 'wins! Paper covers Rock!', player1_name, 'has lost!')
    player2_score += 1
   elif player2_choice == 'S':
     print(player1_name, 'wins! Rock smashes Scissors!', player2_name, 'has lost!')
     player1_score += 1
   else:
     print('Invalid input. Please choose R, P, or S.')
  elif player1_choice == 'P':
    if player2_choice == 'R':
      print(player1_name, 'wins! Paper cover Rock!', player2_name, 'has lost!')
      player1_score += 1
    elif player2_choice == 'P':
     print('It is a tie!', player1_name, 'and', player2_name, 'both chose Paper!')
    elif player2_choice == 'S':
      print( player2_name, 'wins! Scissors! cuts the paper ', player1_name, 'has lost!')
      player2_score += 1
    else:
     print('Invalid input. Please choose R, P, or S.')
  elif player1_choice == 'S':
    if player2_choice == 'R':
     print(player2_name, 'wins! Rock smashes Scissors!', player1_name, 'has lost!')
    player2_score += 1
  elif player2_choice == 'P':
     print(player1_name, 'wins! Scissors cuts the paper!', player2_name, 'has lost!')
     player1_score += 1
  elif player2_choice == 'S':
     print('It is a tie!', player1_name, 'and', player2_name, 'both chose Scissors!')
  else:
    print('Invalid input. Please choose R, P, or S.')
    players_attempts += 1
    continue
  
  print(player1_name, 'you have', player1_score, 'and', player2_name, 'you have', player2_score)

  if player2_score == 3 or player1_score == 3:
    if player1_score == 3:
      print(player1_name, 'You have won by', player1_score)
    else:
      print(player2_name, 'you have won by', player2_score)
      break
    print('The game is over Thank you for playing')
    exit()
    
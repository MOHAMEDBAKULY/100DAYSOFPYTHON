from getpass import getpass as input

print('Welcome🎊 to the Rock, Paper, Scissors game!')
print('The rules are simple:')
print('The game is played between two players, each player chooses one of the three options: Rock, Paper, or Scissors.')
print()
print('If both players choose the same option, it is a tie.')
print('We will use R for Rock, P for Paper, and S for Scissors.')
print()
player1_name = input('Player 1, please enter your name: ')
print('Welcome to the game', player1_name)
player2_name = input('Player 2, please enter your name: ')
print('Welcome to the game', player2_name)
print()
print('Let the game begin!')
player1_choice = input(player1_name + ' please choose R, P, or S: ')
print()
player2_choice = input(player2_name + ' please choose R, P, or S: ')

if player1_choice == 'R':
  if player2_choice == 'R':
   print('It is a tie!', player1_name, 'and', player2_name, 'both chose Rock!')
  elif player2_choice == 'P':
   print(player2_name, 'wins! Paper covers Rock!', player1_name, 'loses!')
  elif player2_choice == 'S':
     print(player1_name, 'wins! Rock smashes Scissors!', player2_name)
  else:
     print('Invalid input. Please choose R, P, or S.')
elif player1_choice == 'P':
  if player2_choice == 'R':
    print(player1_name, 'wins! Paper cover Rock!', player2_name, 'loses')
  elif player2_choice == 'P':
   print('It is a tie!', player1_name, 'and', player2_name, 'both chose Paper!')
  elif player2_choice == 'S':
   print( player2_name, 'wins! Scissors! cuts the paper ', player1_name, 'loses!')
  else:
     print('Invalid input. Please choose R, P, or S.')
elif player1_choice == 'S':
  if player2_choice == 'R':
    print(player2_name, 'wins! Rock smashes Scissors!', player1_name, 'loses!')
  elif player2_choice == 'P':
   print(player1_name, 'wins! Scissors cuts the paper!', player2_name, 'loses!')
  elif player2_choice == 'S':
   print('It is a tie!', player1_name, 'and', player2_name, 'both chose Scissors!')
  else:
   print('Invalid input. Please choose R, P, or S.')
      
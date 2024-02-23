# import os 

# for i in range(1, 500, 2):
#  print(i)
# os.system('clear')

# import os ,time

# for i in range(1, 10):
#   print('Loading', i)
#   time.sleep(2)
# os.system('clear')
# your_name = input('Enter your name: ')
# print('Hello, ' + your_name)


# from replit import
# import audio
# import os, time

# def play():
#   source = audio.play_file('audio.wav')
#   source.paused = False # unpause the playback
#   while True:
#     User_stop = int(input('Press 2 to stop and go back to the menu: '))
#     # Start taking user input and doing something with it
#     if User_stop == 2:
#         source.paused = True
#         return
#     else:
#       continue
#       print('Invalid Input: only press 1 ,2  or 3')




# while True:
#   # clear the screen 
#   os.system('clear')
#   print('Your Favourite Music Player')
#   time.sleep(1)

#   # Show the menu
#   user_name = input('Enter your name: ')
#   time.sleep(1)
#   print('Hello, ' + user_name, 'We know your taste')
#   time.sleep(1)
#   print('Press 1 to Play')
#   time.sleep(1)
#   print('Press 2 to Exit')
#   time.sleep(1)
#   # take user's input
#   User_Choice = int(input('Enter your choice: '))

#   # check whether you should call the play() subroutine depending on user's input
#   if User_Choice == 1:
#     print(user_name, 'Start Listeing')
#     play()
#   elif User_Choice == 2:
#     print(user_name, 'You have paused the music')
#     exit()
#   else:
#     print('Invalid Input:' 'only press 1 or 2')
#     continue
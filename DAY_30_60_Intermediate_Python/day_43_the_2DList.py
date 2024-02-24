import random

print('The bingo random card numbers Generator')
print()

bingo = []

def generateRandomNumbers():
  num = random.randint(1,90)
  return num

def prettyPrint():
  for row in bingo:
    print(row)


numbers = []
for i in range(8):
  numbers.append(generateRandomNumbers())

numbers.sort()

bingo = [
    [numbers[0], numbers[1], numbers[2]],
    [numbers[3], "BINGO", numbers[4]],
    [numbers[5], numbers[6], numbers[7]]
]

prettyPrint()






# my2Dlist = [
#        ['Dr.Juma', 'Pyschology', 'Nairobi Hospital'],
#       ['Dr.Kamau', 'Oncology', 'Nairobi West Hospital'],
#        ['Dr.Sheyma', 'Pediatric', 'Kenyatta Hospital'],
#        ['Dr.Odhiambo', 'Pyschiatry', 'Mathare hospital']
# ]

# my2Dlist[2][1] = 'Surgery'
# # my2Dlist = ['Dr.Ade', 'Surgery', 'Karen Hospital']

# print(my2Dlist[2])

# e2DList = [ ["Johnny", 21, "Mac"],
#              ["Sian", 19, "PC"],
#              ["Gethin", 17, "PC"]
#          ]

# print(e2DList[1][1])
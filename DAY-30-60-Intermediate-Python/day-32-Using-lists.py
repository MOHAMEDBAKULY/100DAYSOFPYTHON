# timetable = ["Computer Science", "Math", "English", "Art", "Sport", "Home Science", "Netwowks", "Biology"]

# for lesson in timetable:
#   print(lesson)

# print()
# timetable[0] = "Information Technolgy"

# print(timetable[0])
# print(timetable[4])
# print(timetable[1])
# print(timetable[3])
# print(timetable[5])
# print(timetable[2])

# colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet"]

# print(f"The first color is {colors[1]}")

# colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Violet"]
# print(f"The first color is {colors[4]}")

# groceryList = ["bananas", "bread", "milk", "eggs", "juice", "cheese"]
# print(f"The first grocery item to buy is {groceryList[1]}.")

import random
red = "\033[0;31m"
reset = "\033[0m"

gretting_in_kenya = [" Good morning","Habari ya asubuhi","Wega maitu","Moni kik","Yaa mûnene","Shikamoo isukuti","Chamgei osusumei"
,"Subax wanaagsan","Supa la ng'wanä","Mwariama rĩa rũrĩmbo","Eitwe piene" ,"Vua ng'uwo","Mbarire rima","Ekitela komok","Naitae lenye"
,"Ebitap toñ","Awoyo wase","Erika ndirii","Akkam ji'aa","Mago marach","Salamu chunge","Wema omwanya","Abariza bonje","Ndiarwa mweri", "Embarua tora", "Wabere ng’aya", "Chemonges elng’at"
,"Sabato e tommes", "Tug’asiele ngetone", "Lenalije pakina"]

greeting = random.randint(1,31)
print(f"""One of many ways you will be greeted in kenya in the morning :

{red}{gretting_in_kenya[greeting]: ^34}{reset}""")
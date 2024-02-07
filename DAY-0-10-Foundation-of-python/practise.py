yellow = "\033[33m"
blue = "\033[34m"
purple = "\033[35m"
reset = "\033[0m"

for day in range(1,31):
    if day <= 10:
     print(yellow,"Today is day", day, "of 30 day",reset)
    elif day > 10 and day <= 20:
     print(blue,"Today is day", day, "of 30 day",reset)
    else:
     print(purple,"Today is day", day, "of 30 day",reset)
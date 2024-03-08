import datetime

print("The Event Countdown Timer")
print()
user_name = input("What is your name? ")
print(f"Hi {user_name}!")
print()
event = input("What event are you looking forward to  ")
day = int(input("On which day> " ))
month = int(input("The Month> " ))
year = int(input("The Year>  " ))
print()

event_date = datetime.date(year, month, day)
date_today = datetime.date.today()
difference = event_date - date_today
difference = difference.days

if event_date == date_today:
  print(f"🎉🎉{event} is today! 🎉🎉")
if difference > 0:
  print(f"{event} is in {difference} days")
elif difference < 0:
  print(f"{event} was {difference} days ago")









# my_birth_day = datetime.date(year=1999, month=5, day=3)
# print(f"This is my birthday: ", my_birth_day)


# date_today = datetime.date.today()
# print(f"This is today's date: ", date_today)

# print("What is the date today")

# # day = int(input("Day: "))
# # month = int(input("Month: "))
# # year = int(input("Year: "))

# date_today = datetime.date.today()
# difference = datetime.timedelta(days=30)
# ramadhan = datetime.date(year=2024, month=3, day=11)
# print(f"The date Today is", date_today)
# print(f"The date in 30 days will be", date_today + difference)

# if date_today == ramadhan:
#   print("It's Ramadhan")
# elif date_today > ramadhan:
#   print("Hope Ramadhan was good")
# elif date_today < ramadhan:
#   print("Ramadhan is on the way")

# import datetime

# today = datetime.date.today() 

# holiday = datetime.date(year=2024, month=5, day=3) 

# if holiday > today: 
#   print("Hope you enjoyed it")
# elif holiday < today: 
#   print("Coming soon")
# else:
#   print("HOLIDAY TIME!")

from replit import db
import datetime, time, os



print("Welcome to your personal tweets database")
print()
timeStamp = datetime.datetime.now()

def addTweet():
  tweet = input("What would you like to tweet? ") 
  tag = input("What tag would you like to add? ")
  db[timeStamp] = [tweet, tag]
  print("Tweet added")
  time.sleep(1)
  os.system("clear")

def viewTweets():
 matches = db.prefix("timestamp")
 matches = matches[::-1]
 option = input("""Show 10 tweets at a time
       1: yes
       2: no
       your action:>  """).lower()
 if option == "1":
    keys = db.keys()
    for key in keys:
      print(f"""{key}: {db[key]}""")
 elif option == "2":
   
  time.sleep(1)
  os.system("clear")



while True:
   tweet_actions = input("""
   Actions to use your tweet database
      1: Add a tweet
      2: View tweets
         your action:>  """)
   if tweet_actions == "1":
     addTweet()
   elif tweet_actions == "2":
    viewTweets()





























# db["Ramadhan1"] = "In two days innshallah"
# db["Ramadhan2"] = "In three days innshallah"
# db["Ramadhan3"] = "In four days innshallah"
# db["Ramadhan4"] = "In five days innshallah"
# db["ramadhan5"] = "In six days innshallah"
# db["Yaummul Eid"] = {"Pray Early": "At the masjid", "Eat": "With family", "Celebrate": "Thank Allah"}


# keys = db.keys()
# for key in keys:
#  print(f"""{key}: {db[key]}""")

# try:
#  value = db["Yeummul Eid"]
#  print(value["Pray Early"])
# except:
#   pass
#   print("We have an error on our side, be paitent as we fix it")


# keys = db.keys()
# for key in keys:
#   print(f"""{key} : {db[key]}""")
# print(keys)
# del db["Ramadhan"]

# matches = db.prefix("Ramadhan")
# print(matches)

import time, os

print("Welcome to the Contact card generator")
print()

user_name = input("What is your name? ").strip().capitalize()
user_birth = input("What is your date of birth? ").strip()
user_phone = input("What is your phone number? ").strip()
user_email = input("What is your email address? ").strip()
user_address = input("Where do you reside? ").strip()
time.sleep(2)
os.system("clear")

contact_card = {"name": user_name, "birth": user_birth, "phone": user_phone, "email": "user_email", "address": user_address}
print()

print(f"""✨Here is your Contact card:✨

  Name: {contact_card["name"]}
  Birth: {contact_card["birth"]}
  Phone: {contact_card["phone"]}
  Email: {contact_card["email"]}
  Residence: {contact_card["address"]}
  """)



# friday_activies = {
#   "5:25" : "Ignored my Alarm did not pray Fajr",
#   "8:30" : "Get out of bed and brushed",
#   "9:00" : "Prepared Thambi na Chai for breakfast",
#   "9:30" : "To a cold shower",
#   "10:00" : "Eat Breakfast and dressed up",
#   "10:30" : "Went to the KNLS library",
#   "13:01" : "Went to the Hurlinghum Masjid for jummah",
#   "14:00" : "Back to KNLS libray"
# }

# # print(friday_activies["5:25"])
# friday_activies["14:00"] = "After jummah prayers i came back to the library"
# # print(friday_activies)


# print(f"On Friday I {friday_activies['9:00']} then {friday_activies['13:01']} in the afternoon")


# myUser = {"name":"Andy", "age":128, "height": 129}

# # print(myUser["name"])
# myUser["Weight"] = 200;
# print(myUser)
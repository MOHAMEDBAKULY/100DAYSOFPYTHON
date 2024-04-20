# import requests, json
# timezone = "EAT"
# latitude = -1.3190023
# longitude = 36.7927213


# while True:
#  result = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=weathercode,temperature_2m_max,temperature_2m_min&timezone={timezone.upper()}")
#  user = result.json()
#  maxTemp = user["daily"]["temperature_2m_max"][0]
#  minTemp = user["daily"]["temperature_2m_min"][0]

#  getUpdates = input("Get weather updates? (y/n) ")
#  if getUpdates == "y":
#    print("The weather today is as follows: ")
#    print(f"Max temperature: {maxTemp}°C")
#    print(f"Min temperature: {minTemp}°C")
#  elif getUpdates == "n":
#    print("Okay, have a nice day!")
#    break
   



# print(json.dumps(user, indent=2))
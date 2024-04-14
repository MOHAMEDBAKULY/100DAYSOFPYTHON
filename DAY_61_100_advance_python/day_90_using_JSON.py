import json, requests

for i in range(10):
  result = requests.get("https://randomuser.me/api/")
  if result.status_code == 200:
   user = result.json()

   for person in user["results"]:
    filename = f"""{person["name"]["first"].lower()}{person["name"]["last"].lower()}.jpg"""""
    get_image = requests.get(person["picture"]["large"])
    f = open(filename, "wb")
    f.write(get_image.content)
    print(f"Saved as {filename}")
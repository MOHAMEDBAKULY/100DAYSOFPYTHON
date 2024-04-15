import requests, json

while(True):
 result = requests.get("https://icanhazdadjoke.com/", 
 headers={"Accept":"application/json"})
 joke = result.json()

 jk = joke["joke"]
 id = joke["id"]
 print(jk)
  
 userInput = input("""
 Save this joke? (y)
 Load old jokes? (l)
 New joke? (n)
 """).lower()
 if userInput == "y":
   f = open("jokes.txt", "a+")
   f.write(f"{jk} {id}\n")
   f.close()
 elif userInput == "l":
   f = open("jokes.txt", "r")
   print(f.read())
 elif userInput == "n":
   continue
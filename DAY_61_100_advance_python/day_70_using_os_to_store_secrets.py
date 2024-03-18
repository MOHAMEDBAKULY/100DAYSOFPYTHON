import os



while True:
 userName = input("Username: ")
 userPass = input("Password: ")

 if userName == os.environ['ADMINUSERNAME'] and userPass == os.environ["ADMINPASSWORD"]:
   print("Welcome back Admin")
   break
 elif userName == os.environ['USERNAME']  and userPass == os.environ['PASSWORD'] :
   print("Welcome back Guest")
 else:
   print("Invalid Credentials")
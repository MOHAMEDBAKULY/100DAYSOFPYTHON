tvShow = input("What is your Best DC series? ")
if tvShow == "The Flash":
  print("That's the best ever?")
  faveCharacter = input("Who is your favorite character? ")
  if faveCharacter == "Barry Allan":
    print("This is the best Actor! ")
    bestEpisode = input("What is your the best episode? ")
    if bestEpisode == "The Thinker":
      print("You are a true fan!")
      worstVillan = input("Who is the worst villan? ")
      if worstVillan == "Reverse Flash":
         print("He was also the mentor of Barry Allan")
  else:
    print("Nah, Barry Allan is the best")
elif tvShow == "The BlackList":
  print("Wow That was intersting to watch")
  bestActor = input("Who is the best actor? ")
  print("Good Job buddy")
else:
  print("Yeah, that's cool and all…")
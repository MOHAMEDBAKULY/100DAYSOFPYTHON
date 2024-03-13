class character:
  name: None
  health: None
  magic: None

  def __init__(self, name, health, magic):
    self.name = name
    self.health = health
    self.magic = magic

  def print(self):
    print(f"""This the Character
      Name: {self.name}
      Health : {self.health}
      Magic : {self.magic}  """)

class player(character):
  num_of_lives: None
  special_move: None

  def __init__(self, name, health, magic, num_of_lives, special_move):
    self.name = "The Flash"
    self.health = health
    self.magic = magic
    self.num_of_lives = num_of_lives
    self.special_move = special_move

  def print(self):
    print(f"""This the player
      Name: {self.name}
      Health : {self.health}
      Magic : {self.magic}
      Number of Lives : {self.num_of_lives}
      Special Move : {self.special_move}  """)

  def am_i_alive(self):
    if self.num_of_lives > "0":
      print("Yes i'm a live")
    elif self.num_of_lives <= "0":
      print("No")


class enemy(character):
  type: None
  strength:  None

  def __init__ (self, name, health, magic, type, strength):
    self.name = "The Thinker"
    self.health = health
    self.magic = magic
    self.type = type
    self.strength = strength

  def print(self):
    print(f"""This the Enemy
      Name: {self.name}
      Health : {self.health}
      Magic : {self.magic}
      Type : {self.type}
      Strength : {self.strength}  """)

class orc(enemy):
  speed: None

  def __init__ (self, name, health, magic, type, strength, speed):
    self.name = "The OG orc"
    self.health = health
    self.magic = magic
    self.type = type
    self.strength = strength
    self.speed = 300

  def print(self):
    print(f"""This the Enemy
      Name: {self.name}
      Health : {self.health}
      Magic : {self.magic}
      Type : {self.type}
      Strength : {self.strength}
      Speed : {self.speed}  """)

class vampire(enemy):
  day_night: None

  def __init__ (self, name, health, magic, type, strength, day_night):
    self.name = name
    self.health = health
    self.magic = magic
    self.type = type
    self.strength = strength
    self.day_night = day_night

  def print(self):
    print(f"""This the Enemy
      Name: {self.name}
      Health : {self.health}
      Magic : {self.magic}
      Type : {self.type}
      Strength : {self.strength}
      Day/Night : {self.day_night}  """)


character_one = character("The Avatar", "100", "402")
character_one.print()
print()

player_one = player("The Flash", "100", "402", "5", "Super Speed")
player_one.print()
player_one.am_i_alive()
print()

vampire_one = vampire("The Zagora", "100", "402", "Vampire", "200", "Night_type")
vampire_one.print()
print()

vampire_two = vampire("The Bahuma_Giant", "100", "402", "Vampire", "200", "Day_type")
vampire_two.print()
print()

orc_one = orc("The OG orc", "100", "402", "Earth_orc" , "200", "300")
orc_one.print()
print()

orc_two = orc("The Ramp orc", "700", "352", "Sun_orc" , "340", "600")
orc_two.print()
print()


orc_three = orc("The Gavi orc", "90", "323", "Moon_orc" , "553", "736")
orc_three.print()
print()
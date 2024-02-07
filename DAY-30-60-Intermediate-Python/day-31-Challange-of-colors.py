print("Welcome to Day 31 Challenge")
print()


red = "\033[31m"
blue = "\033[34m"
green = "\033[32m"
yellow = "\033[33m"
purple = "\033[35m"
reset = "\033[0m"
 
music = "🎶🎶🎶Music App🎶🎶🎶"
raido = """🔥📻  Radio Gaga"""
queen = "Queen"
prev = "PREV"
next = "NEXT"
pause = "PAUSE"

interfaceOne = f"""{yellow}{music:^35}{reset}\n {raido:^3} \n {yellow}{queen: ^20} {reset} \n 

{prev:^10} \n {green}{next:^20}{reset} \n {purple}{pause:^35}{reset}"""

print(interfaceOne)
print()
print()
print()


welcome = "WELCOME TO"
armbook = "--    ARMBOOK    --"
text = """        Definitely not a rip off of 
               a certian other social 
                      networking site
"""
honest = "Honest."
username = "Username:"
password = "Password:"

interfaceTwo = f"""{welcome:^40} \n {blue}{armbook:^39}{reset} \n
{yellow}{text:>35}{reset}\n {red}{honest:^35}{reset} \n 
{username: ^40}
{password: ^40}
"""

print(interfaceTwo)
# def reverse(value):
#   if value <= 2:
#     print("Done! Recursing is over.")
#     return
#   else:
#     for i in range(value):
#       print("✅", end="")
#     print()
#     reverse(value-2)
    
# reverse(25)

def factorial(num):
  if num == 1:
    return 1
  else:
    return num * factorial(num-1)
    
print(factorial(25))

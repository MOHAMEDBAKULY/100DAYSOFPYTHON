import tkinter as tk

window = tk.Tk()
window.title("First Calculator")
window.geometry("200x200")

answer = 0
lastNumber = 0
operator = None

def typeAnswer(value):
  global answer
  answer = f"{answer}{value}"
  answer = int(answer)
  hello["text"] = answer

def calcAnswer(thisOp):
  global answer, lastNumber, operator
  lastNumber = answer
  answer = 0
  if thisOp == "+":
    operator = "+"
  elif thisOp == "-":
    operator = "-"
  elif thisOp == "*":
    operator = "*"
  elif thisOp == "/":
    operator = "/"
  hello["text"] = answer

def calc():
  global anwser, lastNumber, operator
  print(f"{lastNumber} \t {answer} \t {operator}")
  if operator == "+":
      total = lastNumber + answer
  elif operator == "-":
      total = lastNumber - answer
  elif operator == "*":
      total = lastNumber * answer
  elif operator == "/":
      total = lastNumber / answer
      answer = total 
      hello["text"] = answer


hello = tk.Label(text = answer)
hello.grid(row=0, column=1)

one = tk.Button(text="1", command = lambda: typeAnswer(1))
one.grid(row=1, column=0)

two = tk.Button(text="2", command = lambda: typeAnswer(2))
two.grid(row=1, column=1)

three = tk.Button(text="3", command = lambda: typeAnswer(3))
three.grid(row=1, column=2)

add = tk.Button(text="+", command = lambda:
calcAnswer("+"))
add.grid(row=1, column=3)

minus = tk.Button(text="-", command = lambda:
calcAnswer("-"))
minus.grid(row=1, column=4)

four = tk.Button(text="4", command = lambda: typeAnswer(4))
four.grid(row=2, column=0)

five = tk.Button(text="5", command = lambda: typeAnswer(5))
five.grid(row=2, column=1)

six = tk.Button(text="6", command = lambda: typeAnswer(6))
six.grid(row=2, column=2)

multiply = tk.Button(text="*", command = lambda:
calcAnswer("*"))
multiply.grid(row=2, column=3)

divide = tk.Button(text="/", command = lambda:
calcAnswer("/"))
divide.grid(row=2, column=4)

seven = tk.Button(text="7", command = lambda: typeAnswer(7))
seven.grid(row=3, column=0)

eight = tk.Button(text="8", command = lambda: typeAnswer(8))
eight.grid(row=3, column=1)

nine = tk.Button(text="9", command = lambda: typeAnswer(9))
nine.grid(row=3, column=2)

zero = tk.Button(text="0", command = lambda: typeAnswer(0))
zero.grid(row=4, column=1)

equals = tk.Button(text="=", command = calc)
equals.grid(row=4, column=4)

tk.mainloop()

















# import tkinter as tk

# window = tk.Tk()
# window.title("GUI in Python") 
# window.geometry("400x200") 

# label = 0

# def updateLabel():
#   global label
#   number = text.get("1.0","end") 
#   number = int(number) 
#   label += number
#   hello["text"] = label 


# hello = tk.Label(text = label)
# hello.grid(row = 0, column = 1)

# text = tk.Text(window ,height=1, width = 25)
# text.grid(row = 1, column = 1) # New line here

# button = tk.Button(text = "Click me!", command = updateLabel).grid(row = 2, column = 0)

# button = tk.Button(text = "Another Button", command = updateLabel).grid(row = 2, column = 1)

# button = tk.Button(text = "Last one", command = updateLabel).grid(row=2, column=2)

# tk.mainloop()







# import tkinter as tk

# window = tk.Tk()
# window.title("GUI with Python") # Sets the name of the window in the border
# window.geometry("400x200") # Sets the size of the window in pixels

# # label = "Python is fun"
# label = 0

# def updateLabel():
#   global label
#   number = text.get("1.0", "end")
#   number = int(number)
#   label += number
#   hello["text"] = label
#   # text.insert("1.0", label)

# hello = tk.Label(text = label)
# hello.grid(row = 0, column = 1) # Creates a text box
# # hello.pack() # 'pack' places the element on the screen

# text = tk.Text(window, height = 1, width = 30)
# text.grid(row = 1, column = 1)
# # text.pack(side = tk.LEFT)
# # text.insert("1.0", label)

# # button = tk.Button(text = "Click me!", command=updateLabel) # Creates a button
# button = tk.Button(text = "Click me!", command=updateLabel).grid(row = 2, column = 0) # Creates a button
# # button.pack()
# button = tk.Button(text = "Welcome Back!", command=updateLabel).grid(row = 2, column = 1)  # Creates a button
# # button.pack()
# button = tk.Button(text = "Add to cart!", command=updateLabel).grid(row = 2, column = 2)  # Creates a button
# # button.pack()
# # button.pack(side = tk.BOTTOM)

# tk.mainloop()
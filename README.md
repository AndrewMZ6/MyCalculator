# MyCalculator
# My first calculator programm
import tkinter as tk

root = tk.Tk()
mainEntry = tk.Entry()
mainEntry.pack()

def typeOne():
    mainEntry.insert(0, 1)

def typeTwo():
    mainEntry.insert(0, 2)

def typeThree():
    mainEntry.insert(0, 3)

def typeFour():
    mainEntry.insert(0, 4)

def typeFive():
    mainEntry.insert(0, 5)

def typeSix():
    mainEntry.insert(0, 6)

def typeSeven():
    mainEntry.insert(0, 7)

def typeEight():
    mainEntry.insert(0, 8)

def typeNine():
    mainEntry.insert(0, 9)

def typeZero():
    mainEntry.insert(0, 0)

def typePlus():
    mainEntry.insert(0, "+")

def typeMinus():
    mainEntry.insert(0, "-")

def typeMultiply():
    mainEntry.insert(0, "*")

def typeDivide():
    mainEntry.insert(0, "/")

def typeReset():
    mainEntry.delete(0, tk.END)

def Calculate():
    x = mainEntry.get()
    L = []
    Q = []
    R = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    D = ("+", "*", "/", "-")
    for i in x:
    	if i in R:
    		L.append(int(i))
    	elif i in D:
    		Q.append(i)

    if Q[0] == "+":
    	z = L[0] + L[1]
    	mainEntry.delete(0, tk.END)
    	mainEntry.insert(0, z)

    elif Q[0] == "-":
    	z = L[0] - L[1]
    	mainEntry.delete(0, tk.END)
    	mainEntry.insert(0, z)

    elif Q[0] == "*":
    	z = L[0] * L[1]
    	mainEntry.delete(0, tk.END)
    	mainEntry.insert(0, z)

    elif Q[0] == "/":
    	z = L[0] / L[1]
    	mainEntry.delete(0, tk.END)
    	mainEntry.insert(0, z)

frame1 = tk.Frame(root)
frame1.pack()

frame2 = tk.Frame(root)
frame2.pack()

buttonOne = tk.Button(frame1, text = "1", width = 3, height = 3, command = typeOne)
buttonOne.grid(row = 0, column = 0)

buttonTwo = tk.Button(frame1, text = "2", width = 3, height = 3, command = typeTwo)
buttonTwo.grid(row = 1, column = 0)

buttonThree = tk.Button(frame1, text = "3", width = 3, height = 3, command = typeThree)
buttonThree.grid(row = 2, column = 0)

buttonFour = tk.Button(frame1, text = "4", width = 3, height = 3, command = typeFour)
buttonFour.grid(row = 0, column = 1)

buttonFive = tk.Button(frame1, text = "5", width = 3, height = 3, command = typeFive)
buttonFive.grid(row = 1, column = 1)

buttonSix = tk.Button(frame1, text = "6", width = 3, height = 3, command = typeSix)
buttonSix.grid(row = 2, column = 1)

buttonSeven = tk.Button(frame1, text = "7", width = 3, height = 3, command = typeSeven)
buttonSeven.grid(row = 0, column = 2)

buttonEight = tk.Button(frame1, text = "8", width = 3, height = 3, command = typeEight)
buttonEight.grid(row = 1, column = 2)

buttonNine = tk.Button(frame1, text = "9", width = 3, height = 3, command = typeNine)
buttonNine.grid(row = 2, column = 2)

buttonZero = tk.Button(frame1, text = "0", width = 3, height = 3, command = typeZero)
buttonZero.grid(row = 0, column = 3)

buttonPlus = tk.Button(frame2, text = "+", width = 3, height = 3, command = typePlus)
buttonPlus.grid(row = 0, column = 0)

buttonMinus = tk.Button(frame2, text = "-", width = 3, height = 3, command = typeMinus)
buttonMinus.grid(row = 0, column = 1)

buttonMultiply = tk.Button(frame2, text = "*", width = 3, height = 3, command = typeMultiply)
buttonMultiply.grid(row = 0, column = 2)

buttonDivide = tk.Button(frame2, text = "/", width = 3, height = 3, command = typeDivide)
buttonDivide.grid(row = 0, column = 3)

buttonResult = tk.Button(frame1, text = "=", width = 3, height = 3, command = Calculate)	
buttonResult.grid(row = 1, column = 3)

buttonReset = tk.Button(frame1, text = "Reset", width = 3, height = 3, command = typeReset)	
buttonReset.grid(row = 2, column = 3)

root.mainloop()

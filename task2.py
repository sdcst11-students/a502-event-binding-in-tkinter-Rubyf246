#!python3

"""
Create a window with 3 entry widgets and 1 button.
The first 2 entry widgets allow the user to enter in the 2 short sides of a right triangle.
When the button is clicked, calculate the length of the hypotenuse and display it in the 3rd entry widget.
Any labels you need for instruction are optional.
"""
#!python3
import tkinter as tk 
from tkinter import *
from tkinter import ttk 

window = tk.Tk()
window.title("Finding Hypotenuse")
eoutput = StringVar()
eoutput.set("Hypotenuse")

def clickFunction(event):

    print(event)
    number1 = s1e.get()
    number1 = float(number1)

    number2 = s2e.get()
    number2 = float(number2)

    answer = ((number1**(2)) + (number2**(2)))**(1/2)
    ce.delete(0,END)
    ce.insert(3,answer)

side1= tk.Label(window, text= "Side 1: ")
side2 = tk.Label(window,text = "Side 2:")

calculate = tk.Button (window,text= "Calculate")
calculate.bind("<Button>",clickFunction)

s1e= tk.Entry(width= 20)
s2e= tk.Entry(width= 20)
ce= tk.Entry(width= 20,  textvariable=eoutput)

side1.grid(row = 1, column = 1)
side2.grid(row = 2, column = 1 )
calculate.grid (row = 3, column = 1)

s1e.grid(row = 1, column = 2)
s2e.grid(row = 2, column = 2)
ce.grid (row = 3, column = 2)

window.mainloop()

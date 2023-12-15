"""
Factoring simple trinomials
Create a user interface using tkinter.
There should be a label indicating instructions for what the user needs to do.
The program will factor a trinomial of the type ax^2 + bx + c, where a, b and c
are coefficients.  For the purposes of this program, a will always be 1.
The user should enter in coefficients for b and c.  Note that if you are factoring
a trinomial of the type ax^2 - bx + c, then b is just a negative number.
There should be a button to factor the trinomial
The program should display the factored form in an Entry widget.

Extension: make the + between a,b and b,c buttons that will toggle
between + and -.
"""

#!python3
import tkinter as tk 
from tkinter import *
from tkinter import ttk 

window = tk.Tk()
window.title("Factoring Simple Trinomials")

FST = tk.Label(window, text= " Factoring Simple Trinomials ")

b = tk.Label(window, text = "b")
c= tk.Label(window, text= "c")

x1 = tk.Label(window,text = " x^2   +")
bentry= tk.Entry (width=10)
x = tk.Label(window,text= " x   +")
centry= tk.Entry(width= 10)
equal = tk.Label(window, text="=")

calculate = tk.Button (window,text= " Calculate ")
ans= tk.Label(window, text= "answer ======")
aentry= tk.Entry(width= 20)

FST.grid(row = 1, column = 1, columnspan= 5)

b.grid(row = 2, column = 2 )
c.grid (row = 2, column = 4)

x1.grid (row = 4, column = 1)
bentry.grid(row = 4, column = 2)
x.grid(row = 4, column = 3)
centry.grid (row = 4, column = 4)
equal. grid (row = 4, column = 5)

calculate.grid (row = 5, column = 1)
ans.grid(row = 5, column = 2)
aentry.grid(row = 5, column = 3, columnspan = 2)


window.mainloop()
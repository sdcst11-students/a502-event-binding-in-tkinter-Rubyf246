"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""
#!python3
import tkinter as tk 
from tkinter import *
from tkinter import ttk

def clickFunction(event):

    n= ne.get()
    sn= se.get()
    g = ge.get()
    infoinsert = print(f"Student name= {n}\nStudent number= {sn}\nGrade= {g}")
    ie.delete(0,END)
    ie.insert(0, infoinsert)

    
window = tk.Tk()
window.title("Student Database")

name = tk.Label(text= "Name: ")
studentnum = tk.Label(text = "Student #: ")
grade = tk.Label(text= "Grade: ")
info = tk.Button (text= "Information: ")


ne= tk.Entry(width= 20)
se= tk.Entry(width= 20)
ge= tk.Entry(width= 20)
ie= tk.Entry(width= 20)
info.bind("<Button>",clickFunction)

name.grid(row = 1, column = 1)
studentnum.grid(row = 2, column = 1 )
grade.grid (row = 3, column = 1)
info. grid (row = 4, column = 1)

ne.grid(row = 1, column = 2)
se.grid(row = 2, column = 2)
ge.grid (row = 3, column = 2)
ie. grid (row = 4, column = 2)


window.mainloop()
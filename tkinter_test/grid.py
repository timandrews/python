from tkinter import *

root = Tk()

myLabel1 = Label(root, text="Hello world")
myLabel2 = Label(root, text="My name is Joe")
myLabel3 = Label(root, text="3rd label")
mylabel4 = Label(root, text='4th label')

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=0, column=1)
myLabel3.grid(row=1, column=0)
mylabel4.grid(row=2, column=3)


root.mainloop()

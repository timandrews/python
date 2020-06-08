from tkinter import *

root = Tk()

entryWidget = Entry(root, width=50, fg='pink', bg='black', borderwidth=10)
entryWidget.grid(row=0, column=0)
entryWidget.insert(0, "Username")

def myClick():
    greeting = 'Hello, ' + entryWidget.get()
    myLabel = Label(root, text=greeting)
    myLabel.grid(row=1, column=0)

myButton = Button(root, text='Enter your name', command=myClick)
myButton.grid(row=0, column=1)

root.mainloop()
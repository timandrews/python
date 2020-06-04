from tkinter import *

root = Tk()

def myClick():
    myLabel = Label(root, text="Look, I clicked the button")
    myLabel.grid(row=0,column=0)

enabledButton = Button(root,
                       text='Click me!',
                       padx=50,
                       pady=50,
                       command=myClick,
                       fg='green',
                       bg='red')

disabledButton = Button(root,
                        text='You cannot click me',
                        state=DISABLED,
                        padx=50,
                        pady=50)

disabledButton.grid(row=1, column=0)
enabledButton.grid(row=1, column=1)

root.mainloop()
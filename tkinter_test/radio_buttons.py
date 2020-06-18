from tkinter import *

root = Tk()
root.title("Testing radio buttons")
root.iconbitmap('final_fantasy_1_D5h_icon.ICO')

TOPPINGS = [
    ("Pepperoni", "Pepperoni"),
    ('Sausage', 'Sausage'),
    ('Mushroom', 'Mushroom'),
    ('Onion', 'Onion')
]

pizza = StringVar()
pizza.set('Pepperoni')

for text, mode in TOPPINGS:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)


def clicked(value):
    mylabel = Label(root, text=value)
    mylabel.pack()


myButton = Button(root, text='Click me!!!', command=lambda: clicked(pizza.get()))
myButton.pack()

root.mainloop()

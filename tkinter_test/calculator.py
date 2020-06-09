from tkinter import *

root = Tk()
root.title("Tim's calculator")

entryText = Entry(root, width=35, borderwidth=5)
entryText.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click_fun(number):
    tempText = entryText.get()
    entryText.delete(0, END)
    entryText.insert(0, str(tempText) + str(number))


def button_clear():
    entryText.delete(0, END)


def button_add_fun():
    # 3 things have to be done here (
    # 1. save the current number,
    # 2. clear the text, allow,
    # 3. allow input of next number)
    first_number = entryText.get()
    global f_num
    global operation
    operation = 'add'
    f_num = int(first_number)
    entryText.delete(0, END)


def button_subtract_fun():
    # 3 things have to be done here (
    # 1. save the current number,
    # 2. clear the text, allow,
    # 3. allow input of next number)
    first_number = entryText.get()
    global f_num
    global operation
    operation = 'subtract'
    f_num = int(first_number)
    entryText.delete(0, END)


def button_multiply_fun():
    # 3 things have to be done here (
    # 1. save the urrent number,
    # 2. clear the text, allow,
    # 3. allow input of next number)
    first_number = entryText.get()
    global f_num
    global operation
    operation = 'multiply'
    f_num = int(first_number)
    entryText.delete(0, END)


def button_divide_fun():
    # 3 things have to be done here (
    # 1. save the current number,
    # 2. clear the text, allow,
    # 3. allow input of next number)
    first_number = entryText.get()
    global f_num
    global operation
    operation = 'divide'
    f_num = int(first_number)
    entryText.delete(0, END)



def button_equal_fun():
    second_number = entryText.get()
    entryText.delete(0, END)

    if operation == 'add':
        entryText.insert(0, f_num + int(second_number))
    if operation == 'subtract':
        entryText.insert(0, f_num - int(second_number))
    if operation == 'multiply':
        entryText.insert(0, f_num * int(second_number))
    if operation == 'divide':
        entryText.insert(0, f_num / int(second_number))


button1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_click_fun(1))
button2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_click_fun(2))
button3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_click_fun(3))
button4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_click_fun(4))
button5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_click_fun(5))
button6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_click_fun(6))
button7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_click_fun(7))
button8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_click_fun(8))
button9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_click_fun(9))
button0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_click_fun(0))

button_add = Button(root, text='+', padx=20, pady=20, command=button_add_fun)
button_subtract = Button(root, text='-', padx=20, pady=20, command=button_subtract_fun)
button_multiply = Button(root, text='x', padx=20, pady=20, command=button_multiply_fun)
button_divide = Button(root, text='/', padx=20, pady=20, command=button_divide_fun)
button_clear = Button(root, text='clr', padx=20, pady=20, command=button_clear)
button_equals = Button(root, text='=', padx=20, pady=20, command=button_equal_fun)

button1.grid(row=1, column=0)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)
button7.grid(row=3, column=0)
button8.grid(row=3, column=1)
button9.grid(row=3, column=2)
button0.grid(row=4, column=1)
button_add.grid(row=4, column=0)
button_subtract.grid(row=4, column=2)
button_clear.grid(row=1, column=3)
button_equals.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

root.mainloop()

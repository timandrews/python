from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Image viewer')
root.iconbitmap('images/final_fantasy_1_D5h_icon.ICO')

# my_img1 = 'images/black_mage.jpg'
# my_img2 = 'images/fighter.png'
# my_img3 = 'images/ninja.png'
# my_img4 = 'images/thief.jfif'

images = ['images/black_mage.jpg', 'images/fighter.png', 'images/ninja.png', 'images/thief.jfif']
my_img1 = ImageTk.PhotoImage(Image.open(images[0]))
my_img2 = ImageTk.PhotoImage(Image.open(images[1]))
my_img3 = ImageTk.PhotoImage(Image.open(images[2]))
my_img4 = ImageTk.PhotoImage(Image.open(images[3]))


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=images[image_number - 1])
    button_forward = Button(root, text='>>', command=lambda: forward(image_number + 1))
    button_back = Button(root, text='<<', command=lambda: back(image_number - 1))

    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=2)


def back():
    global my_label
    global button_forward
    global button_back

my_img = ImageTk.PhotoImage(Image.open( images[0] ))
my_label = Label(image=my_img)
my_label.grid(row=0, column=0, columnspan=3)


button_back = Button(root, text='<<', command=back)
button_exit = Button(root, text='Exit', command=root.quit)
button_forward = Button(root, text='>>', command=lambda: forward(2))

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()

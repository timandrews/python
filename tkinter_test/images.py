from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Images and icons')

# insert favicon
root.iconbitmap('./final_fantasy_1_D5h_icon.ico')

my_image = ImageTk.PhotoImage(Image.open('aspen-leaf.png'))
my_label = Label(image=my_image)

button_quit = Button(root, text='Exit', command=root.quit)

my_label.grid(row=0, column=5)
button_quit.grid(row=10, column=5)

root.mainloop()

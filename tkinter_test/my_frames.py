from tkinter import *
from PIL import ImageTk, Image # PIL is the Pillow Image Library

root = Tk()

# insert favicon
root.iconbitmap('./final_fantasy_1_D5h_icon.ico')

status = Label(root, text='some status')

frame1 = LabelFrame(root, text='This is a frame', padx=5, pady=5)
my_image1 = ImageTk.PhotoImage(Image.open('aspen-leaf.png'))
my_label1 = Label(frame1, image=my_image1)
my_label1.pack()

frame2 = LabelFrame(root, text='This is another frame', padx=5, pady=5)
my_image2 = ImageTk.PhotoImage(Image.open('final_fantasy_1.png'))
my_label2 = Label(frame2, image=my_image2)
my_label2.pack()

frame1.grid(row=0, column=0, padx=10, pady=10)
frame2.grid(row=0, column=1, padx=10, pady=10)
status.grid(row=1, column=1, columnspan=2, sticky=W)

button1 = Button(frame1, )

root.mainloop()

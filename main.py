from tkinter import *
from tkinter import filedialog as fd

root = Tk()
root.title('Root Window')
root.geometry('600x400+50+50')

button_exit = Button(root, text='Exit', command=exit)
button_exit.grid(row=0, column=0, padx=10, pady=10)

button_next = Button(root, text='Next')
button_next.grid(row=0, column=2, padx=10, pady=10)


add_image_button = Button(root, text='Add Image')
add_image_button.grid(row=0, column=1, padx=210)


root.mainloop()

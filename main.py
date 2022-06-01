from tkinter import *
from tkinter import filedialog as fd

root = Tk()
root.title('Root Window')
root.geometry('600x400+50+50')

button_exit = Button(root, text='EXIT', command=exit)
button_exit.grid(row=0, column=0, padx=10, pady=10)

root.mainloop()

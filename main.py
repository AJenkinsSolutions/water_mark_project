from tkinter import *
from tkinter import filedialog as fd
from PIL import ImageTk, Image


def main():
    class Window():
        def __init__(self):
            # Creating window
            self.root = Tk()
            self.root.geometry('600x400+50+50')
            self.root.title('Root Window')
            # Button states
            self.next_button_state = 'disabled'

            #USEFUl vars
            self.filename = None
            self.image = None

            # Navigation buttons
            exit_button = Button(self.root, text='Exit', command=self.Close)
            exit_button.grid(row=0, column=0, padx=10, pady=10)

            button_next = Button(self.root, text='Next', state=self.next_button_state)
            button_next.grid(row=0, column=2, padx=10, pady=10)

            add_image_button = Button(self.root, text='Add Image', command=self.browse_files)
            add_image_button.grid(row=0, column=1, padx=210)

            self.root.mainloop()

        # Function to close the window
        def Close(self):
            """
            Closes the root window
            :return:
            """
            self.root.quit()

        def browse_files(self):
            """
            Assigns file name path to self.filename parameter
            :return:
            """
            self.filename = fd.askopenfilename(initialdir="/",
                                               title="Select a File",
                                               filetypes=(("image files",
                                                           '*.JPG .jpeg .png'),
                                                          ("all files",
                                                           "*.*")))
            self.assign_image(self.resize_image())

        def resize_image(self):
            """
            Takes Self.filename path opens as image
            get: images width and height
            resizes the image by half maintaining aspect ratio
            uses anti aliais to smooth out edges
            :return: resized image object
            """
            raw_image = Image.open(self.filename)
            width, height = raw_image.size
            resized_image = raw_image.resize((int(width / 2), int(height / 2)), Image.ANTIALIAS)
            return resized_image


        def assign_image(self, image):
            """
            Assign our resized image to self.image attribute
            and assign it our label in our root / frame
            :param image: takes our resized image as input
            :return:
            """
            self.image = ImageTk.PhotoImage(image)
            my_label = Label(self.root, image=self.image).grid(row=1, column=1)


    # def browseFiles():
    #     filename = fd.askopenfilename(initialdir="/",
    #                                   title="Select a File",
    #                                   filetypes=(("image files",
    #                                               '*.JPG .jpeg .png'),
    #                                              ("all files",
    #                                               "*.*")))
    #     my_img = ImageTk.PhotoImage(Image.open(str(filename)))
    #     my_label = Label(root, image=my_img)
    #     my_label.grid(row=1, column=1)
    #     # main_label.config(image=my_img, padx=10, pady=10)
    #     # main_label.grid(row=0, column=0)
    # button_exit = Button(root, text='Exit', command=exit)
    # button_exit.grid(row=0, column=0, padx=10, pady=10)
    #
    # button_next = Button(root, text='Next')
    # button_next.grid(row=0, column=2, padx=10, pady=10)
    #
    # add_image_button = Button(root, text='Add Image', command=browseFiles)
    # add_image_button.grid(row=0, column=1, padx=210)
    #
    # frame = LabelFrame(root, text='This is my label frame', padx=10, pady='10')
    # frame.grid(row=1, column=0, columnspan=3)

    # main_label = Label(frame)
    # main_label.grid(row=0, column=0)

    test = Window()


if __name__ == '__main__':
    main()

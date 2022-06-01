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
            # USEFUl vars
            self.filename = None
            self.image = None

            # Configure place holder **refactor later**
            self.placeholder_image = None
            self.config_placeholder()
            #   Frame
            self.main_frame = Frame(self.root, width=307, height=257, highlightbackground="black",
                                    highlightthickness=2).grid(row=1, column=1, pady=30)
            self.main_label = Label(self.main_frame, image=self.placeholder_image).grid(row=1, column=1)



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

        def config_placeholder(self):
            ph_image = Image.open('images/placeholder-image.png')
            ph_width, ph_height = ph_image.size
            resized_ph_image = ph_image.resize((int(ph_width / 2), int(ph_height / 2)), Image.ANTIALIAS)
            self.placeholder_image = ImageTk.PhotoImage(resized_ph_image)

        def browse_files(self):
            """
            Ask open file name func user selects a files
            Assigns file name path to self.filename parameter
            calls resize_image function
            calls assign image function then displays to screen frame

            :return:
            """
            if self.filename == None:
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
            print(width, height)
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

            # Reassigning our main label within a mainframe
            self.main_label = Label(self.main_frame, image=self.image).grid(row=1, column=1)


    test = Window()


if __name__ == '__main__':
    main()

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
            self.edit_button_state = 'disabled'

            # USEFUl vars
            self.filename = None
            self.image = None
            self.main_label = None

            # Configure place holder **refactor later**
            self.placeholder_image = None
            self.config_placeholder()
            #   Frame
            self.main_frame = Frame(self.root, width=307, height=257, highlightbackground="blue", highlightthickness=2)
            self.main_frame.grid(row=1, column=1, pady=10)

            #Placeholder image
            self.placeholder_label = Label(self.main_frame, image=self.placeholder_image)
            self.placeholder_label.grid(row=1, column=1)



            # Navigation buttons
            self.exit_button = Button(self.root, text='Exit', command=self.Close)
            self.exit_button.grid(row=0, column=0, padx=10, pady=10)

            self.button_edit = Button(self.root, text='Edit', state=self.edit_button_state, command=self.edit)
            self.button_edit.grid(row=0, column=2, padx=10, pady=10)

            self.add_image_button = Button(self.root, text='Add Image', command=self.browse_files)
            self.add_image_button.grid(row=0, column=1, padx=210)

            #Edit Attributes
            self.text_entry = None

            #drop down
            self.position_options = ['Center',
                                     'Top Right',
                                     'Top Center',
                                     'Top Left',
                                     'Bottom Right',
                                     'Bottom Middle',
                                     'Bottom Left']

            self.clicked = None
            self.drop = None

            self.submit_edit = None





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
            #Assign classes image attribute
            self.image = ImageTk.PhotoImage(image)
            #Enable next button *refactor*
            self.edit_button_state = 'active'
            self.button_edit.config(state=self.edit_button_state)


            # Reassigning our main label within a mainframe
            self.main_label = Label(self.main_frame, image=self.image).grid(row=1, column=1)
            #Removing the placeholder image
            self.placeholder_label.grid_forget()




        def submit(self):
             text = self.text_entry.get()
             position = self.clicked.get()
             print(text, position)


        def edit(self):

            self.submit_edit_button = Button(self.root, text='Submit', command=self.submit)
            self.submit_edit_button.grid(row=4, column=1, pady=2)

            #show text box
            self.text_entry = Entry(self.root, width=20)
            self.text_entry.grid(row=2, column=1, pady=2)
            self.text_entry.insert(0, 'Enter Desired text')

            #show drop down
            self.clicked = StringVar()
            self.clicked.set(self.position_options[0])

            self.drop = OptionMenu(self.root, self.clicked, *self.position_options)
            self.drop.grid(row=3, column=1, pady=2)









    test = Window()


if __name__ == '__main__':
    main()

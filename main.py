from tkinter import *
from tkinter import filedialog as fd
from PIL import ImageTk, Image, ImageDraw, ImageFont

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

            # Watermark configure
            self.water_mark_text = None
            self.water_mark_placement = None
            # self.image_width = None
            # self.image_height = None
            # self.text_width = None
            # self.text_height = None
            # self.margin = None

            # Configure place holder **refactor later**
            self.placeholder_image = None
            self.config_placeholder()
            #   Frame
            self.main_frame = Frame(self.root, width=307, height=257, highlightbackground="blue", highlightthickness=2)
            self.main_frame.grid(row=1, column=1, pady=10)

            # Placeholder image
            self.placeholder_label = Label(self.main_frame, image=self.placeholder_image)
            self.placeholder_label.grid(row=1, column=1)

            # Navigation buttons
            self.exit_button = Button(self.root, text='Exit', command=self.Close)
            self.exit_button.grid(row=0, column=0, padx=10, pady=10)

            self.button_edit = Button(self.root, text='Edit', state=self.edit_button_state, command=self.edit)
            self.button_edit.grid(row=0, column=2, padx=10, pady=10)

            self.add_image_button = Button(self.root, text='Add Image', command=self.browse_files)
            self.add_image_button.grid(row=0, column=1, padx=210)

            # Edit Attributes
            self.text_entry = None

            # drop down
            self.position_options = ['Center',
                                     'Top Right',
                                     'Top Center',
                                     'Top Left',
                                     'Bottom Right',
                                     'Bottom Center',
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
            pre_watermark_image = raw_image.resize((int(width / 2), int(height / 2)), Image.ANTIALIAS)
            return pre_watermark_image

        def assign_image(self, image):
            """
            Assign our resized image to self.image attribute
            and assign it our label in our root / frame
            :param image: takes our resized image as input
            :return:
            """
            # Assign classes image attribute
            self.image = ImageTk.PhotoImage(image)
            # Enable next button *refactor*
            self.edit_button_state = 'active'
            self.button_edit.config(state=self.edit_button_state)

            # Reassigning our main label within a mainframe
            self.main_label = Label(self.main_frame, image=self.image).grid(row=1, column=1)
            # Removing the placeholder image
            self.placeholder_label.grid_forget()

        def submit(self):
            self.water_mark_text = self.text_entry.get()
            self.water_mark_placement = self.clicked.get()
            print(self.water_mark_text, self.water_mark_placement)

            self.add_water_mark(self.water_mark_text, self.water_mark_placement, self.filename)

        def add_water_mark(self, text, placement, image):

            # Create image object
            opened_image = Image.open(image)

            # Get image size
            image_width, image_height = opened_image.size
            # print('w', image_width)
            # print('h', image_height)

            # Draw Image Object
            draw = ImageDraw.Draw(opened_image)

            watermark_text = text
            font_size_adj = 8
            if len(watermark_text) > 10:
                font_size_adj = 12
            # if len of text is greater then 10 characters we need to in increase this number
            font_size = int(image_width / font_size_adj)


            watermark_font = ImageFont.truetype('/Library/Fonts/Arial.ttf', font_size)
            text_width, text_height = draw.textsize(watermark_text, watermark_font)


            # Placement
            #   Todo Add placement dictionary refactor

            margin = 10

            #Bottom right
            bottom_right = (image_width - text_width - margin), (image_height - text_height - margin)
            #Center
            center = ((image_width / 2) - (text_width/2)), ((image_height/2) - (text_height))

            bottom_left = ((0 + margin), (image_height - text_height - margin))

            #top_left
            top_left = ((0 + margin), (0 + margin))

            #top_right
            top_right = ((image_width - text_width - margin), (0+ margin))

            #Bottom_center
            bottom_center = ((image_width / 2) - (text_width/2), (image_height - text_height - margin))

            top_center = ((image_width / 2) - (text_width/2), (0))


            # TODO add placement coordinates
            if placement == 'Bottom Right':
                placement = bottom_right
            elif placement == 'Center':
                placement = center
            elif placement == 'Bottom Left':
                placement = bottom_left
            elif placement == 'Top Left':
                placement = top_left
            elif placement == 'Top Right':
                placement = top_right
            elif placement == 'Bottom Center':
                placement = bottom_center
            elif placement == 'Top Center':
                placement = top_center





            #draw water mark to center
            draw.text((placement), watermark_text, font=watermark_font)
            #show
            opened_image.show()




        def edit(self):
            self.submit_edit_button = Button(self.root, text='Submit', command=self.submit)
            self.submit_edit_button.grid(row=4, column=1, pady=2)

            # show text box
            self.text_entry = Entry(self.root, width=20)
            self.text_entry.grid(row=2, column=1, pady=2)
            self.text_entry.insert(0, 'hello world')

            # show drop down
            self.clicked = StringVar()
            self.clicked.set(self.position_options[0])

            self.drop = OptionMenu(self.root, self.clicked, *self.position_options)
            self.drop.grid(row=3, column=1, pady=2)

    test = Window()


if __name__ == '__main__':
    main()

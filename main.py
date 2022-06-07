from tkinter import *
from tkinter import filedialog as fd
from PIL import ImageTk, Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt


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

            #edit frame
            self.edit_frame = Frame(self.root, highlightbackground="blue", highlightthickness=2)
            self.edit_frame.grid(row=2, column=0, columnspan=3)




            # Placeholder image
            self.placeholder_label = Label(self.main_frame, image=self.placeholder_image)
            self.placeholder_label.grid(row=1, column=1)

            # Navigation buttons
            self.exit_button = Button(self.root, text='Exit', command=self.Close)
            self.exit_button.grid(row=0, column=0, padx=10, pady=10)

            # Edit button
            self.button_edit = Button(self.root, text='Edit', state=self.edit_button_state, command=self.edit)
            self.button_edit.grid(row=0, column=2, padx=10, pady=10)

            # Add Image
            self.add_image_button = Button(self.root, text='Add Image', command=self.browse_files)
            self.add_image_button.grid(row=0, column=1, padx=210)

            # Edit Window Attributes

            self.text_entry = None
            # drop down
            self.position_options = ['Center',
                                     'Top Right',
                                     'Top Center',
                                     'Top Left',
                                     'Bottom Right',
                                     'Bottom Center',
                                     'Bottom Left']
            # Watermark configure
            self.water_mark_text = None
            self.water_mark_placement = None

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

            self.logo_placement = self.clicked_logo.get()

            self.add_water_mark(self.water_mark_text, self.water_mark_placement, self.filename, self.logo_placement)


        def add_water_mark(self, text, placement, image, logo_placement):



            # Create image object
            opened_image = Image.open(image)
            # Get image size
            image_width, image_height = opened_image.size
            # Draw Image Object
            draw = ImageDraw.Draw(opened_image)

            # User chosen Text
            watermark_text = text

            # Default Font size
            font_size_adj = 8
            if len(watermark_text) > 10:
                font_size_adj = 12

            # If len of text is greater then 10 characters we need to in increase this number
            font_size = int(image_width / font_size_adj)

            # Retrieving our Font sizes from out computer
            watermark_font = ImageFont.truetype('/Library/Fonts/Arial.ttf', font_size)
            text_width, text_height = draw.textsize(watermark_text, watermark_font)

            # Placement
            #Todo Add placement dictionary refactor

            margin = 10
            # Bottom right
            bottom_right = (image_width - text_width - margin), (image_height - text_height - margin)
            # Center
            center = ((image_width / 2) - (text_width/2)), ((image_height/2) - (text_height))
            # Bottom Left
            bottom_left = ((0 + margin), (image_height - text_height - margin))
            # Top_left
            top_left = ((0 + margin), (0 + margin))
            # Top_right
            top_right = ((image_width - text_width - margin), (0 + margin))
            # Bottom_center
            bottom_center = ((image_width / 2) - (text_width/2), (image_height - text_height - margin))
            # Top center
            top_center = ((image_width / 2) - (text_width/2), 0)



            # text Placement
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

            # Draw watermark to image
            draw.text((placement), watermark_text, font=watermark_font)
            # Assign Water mark
            self.watermark_image = opened_image

            size = (500, 100)
            # Create logo object
            self.logo_image = Image.open(self.logo_filename)
            # Create Thumbnail size
            self.logo_image.thumbnail(size)
            logo_width, logo_height = self.logo_image.size
            copied_image = self.watermark_image.copy()

            # Center
            logo_center = (int(image_width / 2) - int(logo_width / 2)), (int(image_height / 2) - int(logo_height))
            # Top_left
            logo_top_left = (0, 0)
            # Top_right
            logo_top_right = (int(image_width - logo_width), 0)
            # Top center
            logo_top_center = (int(image_width / 2) - int(logo_width / 2), 0)

            # Bottom_center
            logo_bottom_center = (int(image_width / 2) - int(logo_width / 2), (image_height - logo_height))
            # Bottom Left
            logo_bottom_left = (int(0), int(image_height - logo_height))
            # Bottom right
            logo_bottom_right = int(image_width - logo_width), int(image_height - logo_height)


            #   logo placement

            if logo_placement == 'Bottom Right':
                logo_placement = logo_bottom_right
            elif logo_placement == 'Center':
                logo_placement = logo_center
            elif logo_placement == 'Bottom Left':
                logo_placement = logo_bottom_left
            elif logo_placement == 'Top Left':
                logo_placement = logo_top_left
            elif logo_placement == 'Top Right':
                logo_placement = logo_top_right
            elif logo_placement == 'Bottom Center':
                logo_placement = logo_bottom_center
            elif logo_placement == 'Top Center':
                logo_placement = logo_top_center


            #TODO Add logo
            # image watermark

            print(copied_image.size)
            copied_image.paste(self.logo_image, (logo_placement))
            copied_image.show()


            # # add watermark
            # copied_image = image.copy()
            # crop_image.thumbnail(size)
            #
            # # base image
            # copied_image.paste(crop_image, (500, 200))
            # # pasted the crop image onto the base image
            # plt.imshow(copied_image)
            # copied_image.show()



            # self.watermark_image.show()
            self.preview(self.watermark_image)

        def preview(self, image):
            """
            Pressing 'Submit' from the Edit window
            triggers preview pop is displayed to the screen
            displaying the image with watermark
            :param image: image from edit window

            """
            # Creating our pop up window
            preview_window = Toplevel()
            preview_window.title('Preview')

            # Assigning our Image
            self.ph = ImageTk.PhotoImage(image)
            # Display for Image
            label = Label(preview_window, image=self.ph)
            # Reference to our image *tkinter garbage collection*
            label.image = self.ph
            label.grid(row=0, column=0)

            save_btn = Button(preview_window, text='Save',command=lambda: self.save(image))
            save_btn.grid(row=1, column=0)

            # Close button
            close_btn = Button(preview_window, text='Close', command=preview_window.destroy)
            close_btn.grid(row=2, column=0, pady=1)

        def save(self, image):
            print('saving')
            image.save('watermark.jpg')

        def browse_Logo_files(self):
            self.logo_filename = fd.askopenfilename(initialdir="/",
                                               title="Select a File",
                                               filetypes=(("image files",
                                                           '.png'),
                                                          ("all files",
                                                           "*.*")))
            print(self.logo_filename)

            # Assign our reszied logo readyt for implementing
            # self.resized_logo = self.resize_logo()
            # self.thumbnail_logo

        def resize_logo(self):

            # get the dimensions of our logo
            raw_logo = Image.open(self.logo_filename)
            logo_width, logo_height = raw_logo.size
            print(logo_height, logo_width)

            #get the orignal images dimensions
            raw_image = Image.open(self.filename)
            width, height = raw_image.size
            print(width, height)

            # we want to make the logo 1/3 the size of the orignal image
            resized_logo = raw_logo.resize((int(width / 3), int(height / 3)), Image.ANTIALIAS)
            return resized_logo


        def edit(self):
            """
            EDIT: Displays Text Entry, Drop Down Options Menu, Submit Button]
            Text Entry: Gets user input string to be displayed as watermark
            Drop Down: Lets user choose between options displayed in drop down list
            Submit: Triggers preview Pop up window of watermakred image
            """

            # LOGO: Add Button
            self.add_logo = Button(self.edit_frame, text='Add Logo', command=self.browse_Logo_files)
            self.add_logo.grid(row=0, column=1, padx=10)

            # LOGO: Drop Down
            self.clicked_logo = StringVar()
            self.clicked_logo.set(self.position_options[0])
            self.drop_logo = OptionMenu(self.edit_frame, self.clicked_logo, *self.position_options)
            self.drop_logo.grid(row=1, column=1, pady=2, padx=10)






            # Text: Entry Box
            self.text_entry = Entry(self.edit_frame, width=10)
            self.text_entry.grid(row=0, column=0, pady=2, padx=10)
            self.text_entry.insert(0, 'hello world')

            # Text: Drop down
            self.clicked = StringVar()
            self.clicked.set(self.position_options[0])
            self.drop = OptionMenu(self.edit_frame, self.clicked, *self.position_options)
            self.drop.grid(row=1, column=0, pady=2, padx=10)

            # Submit Button
            self.submit_edit_button = Button(self.root, text='Submit', command=self.submit)
            self.submit_edit_button.grid(row=4, column=1, pady=2)

    test = Window()


if __name__ == '__main__':
    main()

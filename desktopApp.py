from tkinter import *
from tkinter import filedialog
import tkinter.font as font
from PIL import Image, ImageTk
from main import calculate
from createArrow import createImage

# Create the main window
root = Tk()
root.title("Image Processor")

# Set the window size
root.geometry("1280x800")

# Create left and right frames
left_frame = Frame(root)
left_frame.pack(side=LEFT, padx=10, pady=10)

right_frame = Frame(root)
right_frame.pack(side=RIGHT, padx=10, pady=10)

# Create a label for displaying the image
image_label = Label(left_frame)
image_label.pack(padx=10, pady=10)

#create a label for displaying the output image
result_image_label = Label(left_frame)
result_image_label.pack( padx=10, pady=0)


# Function for opening an image file
def open_image():
    # Prompt the user to select an image file
    clear_message()
    global image_obj
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        # Load the image file and display it in the label
        image = Image.open(file_path)
        image = image.resize((350, 350))
        image_obj = image
        image = ImageTk.PhotoImage(image)
        image_label.configure(image=image)
        image_label.image = image
        

# Create the "Open Image" button
open_button = Button(left_frame, text="Open Image", command=open_image)
open_button.pack(side=LEFT, padx=10, pady=10)

# Create the dropdown menu
options = ["white", "black"]
player_option = StringVar()
player_option.set(options[0])
dropdown_menu = OptionMenu(left_frame, player_option, *options)
dropdown_menu.pack(side=LEFT, padx=10, pady=10)

# Create the time input box
time_var = StringVar()
time_var.set("3000")
time_input = Entry(left_frame, textvariable=time_var)
time_input.pack(side=LEFT, padx=10, pady=10)

#create two fonts
fontLarge = font.Font(size= 10)
fontSmall = font.Font(size = 20)

# Function for submitting the processed image
def submit_image():
    clear_message()
    result_image_label.configure(image = None)
    result_image_label.image = None
    player_option_value = player_option.get()
    time_value = int(time_var.get())
    print("player option:",player_option_value)
    print("time value:",time_value)
    clear_message()
    bestMove,fenString,depthMessage = calculate(image_obj, player_option_value[0], time_value)
    display_message(bestMove + depthMessage)
    arrow_image = createImage(fenString, bestMove)
    
    img = Image.open('temp.png')
    img = ImageTk.PhotoImage(img)
    result_image_label.configure(image=img)
    result_image_label.image = img

# Create the "Submit" button
submit_button = Button(left_frame, text="Submit", command=submit_image)
submit_button.pack(side=LEFT, padx=10, pady=10)

#function to display message in text box
def display_message(message):
    clear_message()
    message_text['font'] = fontLarge
    message_text.insert(END, message)

#function to clear the message box
def clear_message():
    message_text.delete("1.0", END)



# Create the scrollable text display area
message_text_scrollbar = Scrollbar(root)
message_text_scrollbar.pack(side=LEFT, fill=Y)

message_text = Text(root, height=800,width = 200, yscrollcommand=message_text_scrollbar.set)
message_text.pack(padx=30, pady=10)

message_text_scrollbar.config(command=message_text.yview)

# Start the main event loop
root.mainloop()
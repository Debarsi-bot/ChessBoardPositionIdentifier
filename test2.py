import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
# from main import calculate
# from createArrow import createImage

# Create the main window
root = tk.Tk()
root.title("Image Processor")

# Set the window size
root.geometry("1280x960")

# Create left and right frames
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, padx=10, pady=10)

right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

# Create a label for displaying the image
image_label = tk.Label(left_frame)
image_label.pack( padx=10, pady=0)

result_image_label = tk.Label(right_frame)
result_image_label.pack( padx=10, pady=0)

# Function for opening an image file
def open_image():
    # Prompt the user to select an image file
    global image_obj
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        # Load the image file and display it in the label
        image = Image.open(file_path)
        image = image.resize((500, 500))
        image_obj = image
        image = ImageTk.PhotoImage(image)
        image_label.configure(image=image)
        image_label.image = image
        

# Create the "Open Image" button
open_button = tk.Button(left_frame, text="Open Image", command=open_image)
open_button.pack(side=tk.LEFT, padx=10, pady=10)

# Create the dropdown menu
options = ["white", "black"]
player_option = tk.StringVar()
player_option.set(options[0])
dropdown_menu = tk.OptionMenu(left_frame, player_option, *options)
dropdown_menu.pack(side=tk.LEFT, padx=10, pady=10)

# Create the time input box
time_var = tk.StringVar()
time_var.set("3000")
time_input = tk.Entry(left_frame, textvariable=time_var)
time_input.pack(side=tk.LEFT, padx=10, pady=10)

# Function for submitting the processed image
def submit_image():
    clear_message()
    player_option_value = player_option.get()
    time_value = int(time_var.get())
    print("player option:",player_option_value)
    print("time value:",time_value)
    message_text.delete("1.0", tk.END)
    # bestMove,fenString,depthMessage = calculate(image_obj, player_option_value[0], time_value)
    # display_message(bestMove + depthMessage)
    # arrow_image = createImage(fenString, bestMove)
    # with open("chessboard.svg", "w") as f:
    #     f.write(arrow_image)


# Create the "Submit" button
submit_button = tk.Button(left_frame, text="Submit", command=submit_image)
submit_button.pack(side=tk.LEFT, padx=10, pady=10)

#function to display message in text box
def display_message(message):
    clear_message()
    message_text.insert(tk.END, message)

#function to clear the message box
def clear_message():
    print("message cleared")
    message_text.delete("1.0", tk.END)

# # Create a label for displaying the message
# message_label = tk.Label(right_frame, text="Message:")
# message_label.pack(side = tk.LEFT, padx=10, pady=10)

# Create the scrollable text display area
message_text_scrollbar = tk.Scrollbar(root)
message_text_scrollbar.pack(side=tk.LEFT, fill=tk.Y)

message_text = tk.Text(root, height=30, yscrollcommand=message_text_scrollbar.set)
message_text.pack(padx=10, pady=10)

message_text_scrollbar.config(command=message_text.yview)

# Start the main event loop
root.mainloop()
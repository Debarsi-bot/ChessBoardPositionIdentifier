import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

# Function to open an image
def open_image():
    # Open a file dialog to select an image file
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])

    # Load the image using PIL
    image = Image.open(file_path)

    # Resize the image if needed (adjust the dimensions as desired)
    image = image.resize((300, 300))

    # Convert the PIL image to Tkinter-compatible format
    tk_image = ImageTk.PhotoImage(image)

    # Update the image label
    image_label.configure(image=tk_image)
    image_label.image = tk_image

# Function to submit the form
def submit_form():
    # Get the selected option from the dropdown menu
    selected_option = dropdown.get()

    # Get the entered number from the number input
    entered_number = number_entry.get()

    # Perform some processing based on the inputs
    output_text = f"Selected option: {selected_option}\nEntered number: {entered_number}"

    # Update the output text box
    output_textbox.delete("1.0", tk.END)
    output_textbox.insert(tk.END, output_text)

# Create a Tkinter window
window = tk.Tk()
window.title("Image App")

# Create left and right frames
left_frame = tk.Frame(window)
left_frame.pack(side=tk.LEFT, padx=10, pady=10)

right_frame = tk.Frame(window)
right_frame.pack(side=tk.RIGHT, padx=10, pady=10)

# Create the "Open Image" button
open_image_button = tk.Button(left_frame, text="Open Image", command=open_image)
open_image_button.pack()

# Create the dropdown menu
dropdown_label = tk.Label(left_frame, text="Select Option:")
dropdown_label.pack()

options = ["Option 1", "Option 2", "Option 3"]  # Replace with your desired options
dropdown = tk.StringVar(left_frame)
dropdown.set(options[0])  # Set the default option

dropdown_menu = tk.OptionMenu(left_frame, dropdown, *options)
dropdown_menu.pack()

# Create the number input button
number_label = tk.Label(left_frame, text="Enter a Number:")
number_label.pack()

number_entry = tk.Entry(left_frame)
number_entry.pack()

# Create the submit button
submit_button = tk.Button(left_frame, text="Submit", command=submit_form)
submit_button.pack()

# Create the image label
image_label = tk.Label(right_frame)
image_label.pack()

# Create the output text box
output_textbox = tk.Text(right_frame, height=10, width=30)
output_textbox.pack()

# Start the Tkinter event loop
window.mainloop()

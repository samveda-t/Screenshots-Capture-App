import tkinter as tk
from tkinter import filedialog
from screenshot import take_screenshot

# Global variable to store the screenshot
screenshot_image = None

def create_ui(root):
    global screenshot_image
    
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    take_screenshot_button = tk.Button(frame, text="Take Screenshot", command=lambda: take_and_show_screenshot())
    take_screenshot_button.pack(pady=5)

    save_button = tk.Button(frame, text="Save Screenshot", command=lambda: save_screenshot())
    save_button.pack(pady=5)

def take_and_show_screenshot():
    global screenshot_image
    screenshot_image = take_screenshot()  # Capture the screenshot and store it

def save_screenshot():
    global screenshot_image
    if screenshot_image is not None:
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                   filetypes=[("PNG files", "*.png"),
                                                              ("JPEG files", "*.jpg"),
                                                              ("All files", "*.*")])
        if file_path:
            # Save the screenshot to the selected path
            screenshot_image.save(file_path)  # Save the image
            print(f"Screenshot saved to: {file_path}")  # Confirmation message
    else:
        print("No screenshot to save. Please take a screenshot first.")

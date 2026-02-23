# Program Name: Assignment3.py
# Course: IT3883 / Section W01
# Student Name: Jermaine Ayuk
# Assignment Number: Lab 3
# Due Date: 02/28/2026
# Purpose: This program creates a GUI that converts Miles per Gallon (mpg)
#          into Kilometers per Liter (km/l). The conversion updates in real time
#          as the user types, and the program safely handles invalid input.
# Resources Used: Tkinter documentation, class notes, and assistance from AI
#                 (concept explanation only, all code written by me).

import tkinter as tk

# Conversion factor: 1 mpg = 0.425143707 km/l
CONVERSION_FACTOR = 0.425143707

def convert_mpg_to_kml(event):
    """
    This function runs every time the user types in the mpg entry box.
    It attempts to convert the input to a float. If the input is invalid,
    the output label is cleared instead of crashing.
    """
    user_input = mpg_entry.get()

    try:
        mpg_value = float(user_input)
        kml_value = mpg_value * CONVERSION_FACTOR
        result_label.config(text=f"{kml_value:.4f} km/l")
    except ValueError:
        # If the user types letters or leaves it blank, clear the output
        result_label.config(text="")

# Create the main window
window = tk.Tk()
window.title("MPG to KM/L Converter")

# Create and place labels and entry box
mpg_label = tk.Label(window, text="Miles per Gallon (mpg):")
mpg_label.pack()

mpg_entry = tk.Entry(window)
mpg_entry.pack()

# Bind key release so the conversion updates as the user types
mpg_entry.bind("<KeyRelease>", convert_mpg_to_kml)

result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Start the GUI loop
window.mainloop()

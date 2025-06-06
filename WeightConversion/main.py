import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

def convert():
   fahrenheit_input = entry_int.get()
   celsius = round((5/9) * (fahrenheit_input - 32), 2)
   #celsius = round(celsius, 2)
   output_string.set(f"{celsius}°C")

# window
window = ttk.Window(themename = "solar")
window.title("Demo")
window.geometry("375x150")

# title
title_label = ttk.Label(master = window, text = "Fahrenheit to Celsius", font = "Helvetica 24 bold")
title_label.pack()

input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_int)
button = ttk.Button(master = input_frame, text = "Convert", command = convert)
entry.pack(side = "left", padx = 10)
button.pack(side = "left")
input_frame.pack(pady = 10)

output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = "Output", font = "Helvetica 24", textvariable = output_string)
output_label.pack(pady = 5)

# run
window.mainloop()
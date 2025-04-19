# Importing Tkinter
import tkinter as tk
from tkinter import ttk

# Importing basic style library [Temporarirly]
import sv_ttk
 
# Initalize window
window = tk.Tk()
window.title("To-do List")
window.geometry("400x400")

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.rowconfigure(2, weight=1)

# Creation of seperator
seperator = ttk.Separator(window, orient="horizontal")

# Creation of lables
highPriorityLabel = ttk.Label(window, text=" High priority task ")
normalPriorityLabel = ttk.Label(window, text=" Normal priority task ")
lowPriorityLabel = ttk.Label(window, text=" Low priority task ")

# Grid Layout
highPriorityLabel.grid(row=0, column=0, pady=5)
normalPriorityLabel.grid(row=0, column=1, pady=5)
lowPriorityLabel.grid(row=0, column=2, pady=5)
seperator.grid(row=2, columnspan=3, sticky="nsew", pady=10)

# Setting the standard theme
sv_ttk.set_theme("dark")


window.mainloop()
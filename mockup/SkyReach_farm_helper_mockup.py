import tkinter as tk
from tkinter import ttk


# create root window so other windows can be freely created and destroyed
root = tk.Tk()
# hide from user
root.withdraw()

# setup menu window
menu_window = tk.Toplevel(root)
menu_window.title('SkyReach AI Farming Assistant')
menu_window_width = 640
menu_window_height = 480
menu_window.resizable(False, False)

# attributes
menu_window.attributes('-topmost', 1)

# get screen size variables
screen_width = menu_window.winfo_screenwidth()
screen_height = menu_window.winfo_screenheight()

# center on screen
center_x = int(screen_width/2 - menu_window_width / 2)
center_y = int(screen_height/2 - menu_window_height / 2)
menu_window.geometry(f'{menu_window_width}x{menu_window_height}+{center_x}+{center_y}')







menu_window.mainloop()

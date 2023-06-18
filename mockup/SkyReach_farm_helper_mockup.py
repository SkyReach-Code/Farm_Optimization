import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askokcancel, showinfo, showwarning


# create root window so other windows can be freely created and destroyed
root = tk.Tk()
# hide from user
root.withdraw()


# create images
menu_image_HAND_IN_FIELDS = tk.PhotoImage(file='./images/menu_image_HAND_IN_FIELDS.png')


# create icons
icon_add = tk.PhotoImage(file='./icons/icons8-plus-48.png')
icon_edit = tk.PhotoImage(file='./icons/icons8-edit-48.png')
icon_sun = tk.PhotoImage(file='./icons/icons8-sun-48.png')
icon_leave = tk.PhotoImage(file='./icons/icons8-emergency-exit-48.png')
icon_save = tk.PhotoImage(file='./icons/icons8-save-48.png')


# general code
def return_to_menu():
    situation_editor.withdraw()
    menu_window.state('normal')


def new_situation():
    menu_window.withdraw()
    situation_editor.state('normal')
    situation_editor.lift()
    situation_editor.focus()
    situation_editor.geometry(f'{situation_editor_width}x{situation_editor_height}'
                              f'+{situation_editor_center_x}+{situation_editor_center_y}')
    situation_editor.update()


def save_situation():
    if askokcancel(title='Verify Information',
                   message='Please make sure that all required information is filled in, as the advice' +
                           'generator may run into issues otherwise.'):
        return_to_menu()



# setup menu window
menu_window = tk.Toplevel(root)
menu_window.title('SkyReach AI Farming Assistant')
menu_window_width = 640
menu_window_height = 480
menu_window.resizable(False, False)

menu_window.attributes('-topmost', 1)
# removes the button bar up top, making this look moreso like a splash screen
menu_window.overrideredirect(True)

# get screen size variables
screen_width = menu_window.winfo_screenwidth()
screen_height = menu_window.winfo_screenheight()

# center on screen
center_x = int(screen_width/2 - menu_window_width / 2)
center_y = int(screen_height/2 - menu_window_height / 2)
menu_window.geometry(f'{menu_window_width}x{menu_window_height}+{center_x}+{center_y}')


# menu items

menu_window_background_label = tk.Label(menu_window, image=menu_image_HAND_IN_FIELDS)
menu_window_background_label.pack()

menu_window_new_situation_button = ttk.Button(menu_window, image=icon_add, command=new_situation,
                                              text='Create New Situation', compound='left')
menu_window_new_situation_button.place(x=320, y=200, anchor=tk.CENTER)

menu_window_edit_situation_button = ttk.Button(menu_window, image=icon_edit,
                                               text='Edit Existing Situation', compound='left')
menu_window_edit_situation_button.place(x=320, y=270, anchor=tk.CENTER)

menu_window_advice_button = ttk.Button(menu_window, image=icon_sun,
                                       text='Get Advice for a Situation', compound='left')
menu_window_advice_button.place(x=320, y=340, anchor=tk.CENTER)

menu_window_advice_button = ttk.Button(menu_window, image=icon_leave, command=exit)
menu_window_advice_button.place(x=320, y=430, anchor=tk.CENTER)


# setup situation editor

situationFileName = 'New Situation'

situation_editor = tk.Toplevel(root)
situation_editor.title('SkyReach AI Farm Optimizer: Situation Editor | ' + situationFileName)
situation_editor_width = 800
situation_editor_height = 600
situation_editor.resizable(False, False)


situation_editor_center_x = int(screen_width/2 - situation_editor_width / 2)
situation_editor_center_y = int(screen_height/2 - situation_editor_height / 2)

situation_editor.protocol("WM_DELETE_WINDOW", return_to_menu)


# main content setup
nameInputText = tk.Text(situation_editor, height=1)
nameInputText.place(x=32, y=550, width=(575-32))

saveSituationButton = ttk.Button(situation_editor, text='Save Situation', image=icon_save, compound='left',
                                 command=save_situation)
saveSituationButton.place(x=690, y=560, anchor='center')


# ######## Main Code
situation_editor.withdraw()

root.mainloop()

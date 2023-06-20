import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askokcancel  # , showinfo, showwarning


# create root window so other windows can be freely created and destroyed
root = tk.Tk()
# hide from user
root.withdraw()


# create images
menu_image_HAND_IN_FIELDS = tk.PhotoImage(file='./images/menu_image_HAND_IN_FIELDS_TEXT.png')
editor_image_PLANT_ASSORTMENT_SMALL = tk.PhotoImage(file='./images/editor_image_PLANT_ASSORTMENT_SMALL.png')


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
    situation_editor.geometry(f'{situation_editor_width}x{situation_editor_height}'
                              f'+{situation_editor_center_x}+{situation_editor_center_y}')
    situation_editor.update()
    situation_editor.lift()
    situation_editor.focus()



def save_situation():
    if askokcancel(title='Verify Information',
                   message='Please make sure that all required information is filled in, as the advice' +
                           ' generator may run into issues otherwise.'):
        return_to_menu()


# setup menu window
menu_window = tk.Toplevel(root)
menu_window.title('SkyReach AI Farming Assistant')
menu_window_width = 640
menu_window_height = 480
menu_window.resizable(False, False)

menu_window.attributes('-topmost', True)
# removes the button bar up top, making this look more like a splash screen
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
menu_window_new_situation_button.place(x=320, y=220, anchor=tk.CENTER)

menu_window_edit_situation_button = ttk.Button(menu_window, image=icon_edit,
                                               text='Edit Existing Situation', compound='left')
menu_window_edit_situation_button.place(x=320, y=285, anchor=tk.CENTER)

menu_window_advice_button = ttk.Button(menu_window, image=icon_sun,
                                       text='Get Advice for a Situation', compound='left')
menu_window_advice_button.place(x=320, y=350, anchor=tk.CENTER)

menu_window_leave_button = ttk.Button(menu_window, image=icon_leave, command=exit)
menu_window_leave_button.place(x=320, y=430, anchor=tk.CENTER)


# setup situation editor

situationFileName = 'New Situation'

situation_editor = tk.Toplevel(root, bg='light gray')
situation_editor.title('SkyReach AI Farm Optimizer: Situation Editor | ' + situationFileName)
situation_editor.iconbitmap('./icons/icons8-plus-48.ico')
situation_editor_width = 800
situation_editor_height = 600
situation_editor.resizable(False, False)


situation_editor_center_x = int(screen_width/2 - situation_editor_width / 2)
situation_editor_center_y = int(screen_height/2 - situation_editor_height / 2)

situation_editor.protocol("WM_DELETE_WINDOW", return_to_menu)


# main content setup
nameInputText = tk.Text(situation_editor, height=1)
nameInputText.insert('1.0', 'Please write the Situation name here.')
nameInputText.place(x=32, y=550, width=(575-32))

saveSituationButton = ttk.Button(situation_editor, text='Save Situation', image=icon_save, compound='left',
                                 command=save_situation)
saveSituationButton.place(x=690, y=560, anchor='center')

editorNotebook = ttk.Notebook(situation_editor)
editorNotebook.place(x=0, y=0, relwidth=1, height=525)


# instruction page

editorFrame_instructions = ttk.Frame(editorNotebook, width=800, height=500)
editorFrame_instructions.place(x=0, y=0, relwidth=1, relheight=1)
editorNotebook.add(editorFrame_instructions, text='Instructions')

instructionsTitle = ttk.Label(editorFrame_instructions, font='Garamond 24',
                              text="Welcome to SkyReach's AI Farm Optimizer")
instructionsTitle.place(relx=0.5, y=50, anchor='center')

instructionsText = ttk.Label(editorFrame_instructions, font='Garamond 14',
                             text="INSTRUCTIONS:\nNavigate across all inputs using the bar at the top."
                                  "\nEnter the information as accurately as possible- tabs specified below are"
                                  " required.\nOnce you are finished, press the 'Save Situation'"
                                  " button to save the Situation file.\nYou will then be returned to the main menu,"
                                  "where you can click on 'Get Advice for a Situation' to get said advice "
                                  "for your newly created Situation.\n\n"
                                  "REQUIRED TABS:\n* Budget\n* Location\n* Crop Types"
                                  "\n\nDon't forget to write the Situation's name in the space below!")
instructionsText.config(wraplength=800)
instructionsText.place(y=100, relwidth=1, anchor='nw')


# budget page

editorFrame_budget = ttk.Frame(editorNotebook, width=800, height=500)
editorFrame_budget.place(x=0, y=0, relwidth=1, relheight=1)
editorNotebook.add(editorFrame_budget, text='Budget')


def editor_budget_change(value):
    editor_currentBudgetLabel.config(text='Current budget: $' + str(1000 * int(str(value).split('.')[0])))


editor_currentBudgetLabel = ttk.Label(editorFrame_budget, text='Current budget: $1000')
editor_currentBudgetLabel.place(x=50, y=50)
editor_currentBudgetSlider = ttk.Scale(editorFrame_budget, from_=1, to=2500, command=editor_budget_change)
editor_currentBudgetSlider.place(x=50, y=75, width=700)


def editor_new_budget_change(value):
    editor_newBudgetLabel.config(text='Additional budget for increasing optimization and eco-friendliness: $'
                                      + str(100 * int(str(value).split('.')[0])))


editor_newBudgetLabel = ttk.Label(editorFrame_budget, text='Additional budget for increasing optimization and'
                                                           ' eco-friendliness: $100')
editor_newBudgetLabel.place(x=50, y=125)
editor_newBudgetSlider = ttk.Scale(editorFrame_budget, from_=0, to=700, command=editor_new_budget_change)
editor_newBudgetSlider.place(x=50, y=150, width=700)


# Crop Types page

editorFrame_cropTypes = ttk.Frame(editorNotebook, width=800, height=500)
editorFrame_cropTypes.place(x=0, y=0, relwidth=1, relheight=1)
editorNotebook.add(editorFrame_cropTypes, text='Crop Types')

editor_plantAssortmentLabel = ttk.Label(editorFrame_cropTypes, image=editor_image_PLANT_ASSORTMENT_SMALL)
editor_plantAssortmentLabel.place(x=25, y=25)

editor_cropTypesInstructionsLabel = ttk.Label(editorFrame_cropTypes, font='Garamond 13', wraplength=575,
                                              text='Instructions:\nSelect each type of crop you are growing below.\n'
                                                   'Each crop type has different growing conditions and is either'
                                                   ' supported or inhibited by being grown near specific other types.')
editor_cropTypesInstructionsLabel.place(x=200, y=25, anchor='nw')

editor_cropTypesHorDivider = ttk.Separator(editorFrame_cropTypes, orient='horizontal')
editor_cropTypesHorDivider.place(x=20, width=760, y=200)


# ######## Main Code
situation_editor.withdraw()

root.mainloop()

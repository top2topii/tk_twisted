import tkinter as tk
from tkinter import ttk, scrolledtext, Menu

# Radiobutton Globals # 1
COLOR1 = "Blue" # 2
COLOR2 = "Gold" # 3
COLOR3 = "Red" # 4

# Using a scrolled Text control # 3
scrolW = 30 # 4
scrolH = 3

# for radio_buttons
#global radVar

# Modified Button Click Function 
def clickMe():
    action.configure(text='Hello ' + name.get())

# Radiobutton Callback # 5


# Menu exit
def menu_quit():
    win.quit()
    win.destroy()
    exit()

# create three Radiobuttons
def radiobuttons_build(this_row):

    def radCall():
        radSel=radVar.get()
        if radSel == 1: win.configure(background=COLOR1)
        elif radSel == 2: win.configure(background=COLOR2)
        elif radSel == 3: win.configure(background=COLOR3)
    
    radVar = tk.IntVar()
    rad1 = tk.Radiobutton(win, text=COLOR1, variable=radVar, value=1, command=radCall)
    rad1.grid(column=0, row=this_row, sticky=tk.W)
    rad2 = tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=radCall)
    rad2.grid(column=1, row=this_row, sticky=tk.W)
    rad3 = tk.Radiobutton(win, text=COLOR3, variable=radVar, value=3, command=radCall)
    rad3.grid(column=2, row=this_row, sticky=tk.W)

# Creating three checkbuttons
def checkbutons_build(this_row):
    chVarDis = tk.IntVar()
    check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')
    check1.select()
    check1.grid(column=0, row=this_row, sticky=tk.W)
    chVarUn = tk.IntVar()
    check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn)
    check2.deselect()
    check2.grid(column=1, row=this_row, sticky=tk.W)
    chVarEn = tk.IntVar()
    check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
    check3.select()
    check3.grid(column=2, row=this_row, sticky=tk.W)

# Create a container to hold labels
def labelframe_build(this_row):
    labelsFrame = ttk.LabelFrame(win, text=' Labels in a Frame ')
    labelsFrame.grid(column=0, row=this_row, columnspan=2, padx=20, pady=40)

    # Place labels into the container element – vertically # 3
    ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0)
    ttk.Label(labelsFrame, text="Label2").grid(column=0, row=1)
    ttk.Label(labelsFrame, text="Label3").grid(column=0, row=2)

    for child in labelsFrame.winfo_children():
        child.grid_configure(padx=8, pady=4)

# Menu Build
def menu_build():
    menuBar = Menu(win)
    win.config(menu=menuBar)
    fileMenu = Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label="파일", menu=fileMenu)
    fileMenu.add_command(label="새파일")
    fileMenu.add_separator() # 4
    fileMenu.add_command(label="Exit", command=menu_quit)

    helpMenu = Menu(menuBar, tearoff=0) # 6
    helpMenu.add_command(label="About")
    menuBar.add_cascade(label="Help", menu=helpMenu)

win = tk.Tk()

# Modify adding a Label 
aLabel = ttk.Label(win, text="이름:")
aLabel.grid(column=0, row=0, sticky=tk.W)

# Adding a Textbox Entry widget
name = tk.StringVar() # 6
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1, sticky=tk.W)

ttk.Label(win, text="번호 선택:").grid(column=1, row=0, sticky=tk.W)
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')

numberChosen['values'] = (1, 2, 4, 42, 100) # 4
numberChosen.grid(column=1, row=1) # 5
numberChosen.current(0)

# Adding a Button 
action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=2, row=1)

current_row = 1
# Creating three checkbuttons
current_row += 1
checkbutons_build(this_row=current_row)

# create three Radiobuttons
current_row += 1
radiobuttons_build(this_row=current_row)

# Create a scrolledtext
current_row += 1
scr = scrolledtext.ScrolledText(win, width=scrolW, height=scrolH, wrap=tk.WORD)
scr.grid(column=0, columnspan=3, sticky='WE')

# Create a container to hold labels
current_row += 1
labelframe_build(this_row=current_row)

# Place cursor into name Entry
nameEntered.focus()

menu_build()

win.title("Python GUI")

win.mainloop()
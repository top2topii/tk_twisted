#!/usr/bin/env python2.7
#-*- coding: utf-8 -*-

#from tkinter import *
#import future
import tkinter
import tkinter.ttk, tkinter.messagebox
from twisted.internet import tksupport, reactor

win = tkinter.Tk()

# Install the Reactor support
tksupport.install(win)

# at this point build Tk app as usual using the root object,
# and start the program with "reactor.run()", and stop it
# with "reactor.stop()".

# Modified Button Click Function 
def clickMe():
    action.configure(text='Hello ' + name.get())

# Menu exit
def menu_quit():
    win.quit()
    win.destroy()
    reactor.stop()
    exit()

# Menu Build
def menu_build():
    menuBar = tkinter.Menu(win)
    win.config(menu=menuBar)
    fileMenu = tkinter.Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label="파일", menu=fileMenu)
    fileMenu.add_command(label="새파일")
    fileMenu.add_separator() # 4
    fileMenu.add_command(label="Exit", command=menu_quit)

    helpMenu = tkinter.Menu(menuBar, tearoff=0) # 6
    helpMenu.add_command(label="About")
    menuBar.add_cascade(label="Help", menu=helpMenu)

def on_closing():
    if messagebox.askokcancel("Quit", "프로그램을 끝내시겠습니까?"):
        menu_quit()

# Modify adding a Label 
aLabel = tkinter.ttk.Label(win, text="이름:")
aLabel.grid(column=0, row=0, sticky='W')

# Adding a Textbox Entry widget
name = tkinter.StringVar()
nameEntered = tkinter.ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1, sticky='W')

tkinter.ttk.Label(win, text="번호 선택:").grid(column=1, row=0, sticky='W')
number = tkinter.StringVar()
numberChosen = tkinter.ttk.Combobox(win, width=12, textvariable=number, state='readonly')

numberChosen['values'] = (1, 2, 4, 42, 100) # 4
numberChosen.grid(column=1, row=1) # 5
numberChosen.current(0)

# Adding a Button 
action = tkinter.ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=2, row=1)

menu_build()

win.protocol("WM_DELETE_WINDOW", on_closing)

reactor.run()


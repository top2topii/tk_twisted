#!/usr/bin/env python3
#-*- coding: utf-8 -*-

#from tkinter import *
#import future

import webbrowser
import sys
from sys import platform

import tkinter as tk
from tkinter import ttk, messagebox
from twisted.internet import reactor
import tksupport

from twisted.web.server import Site
from klein import Klein

win = tk.Tk()

# Install the Reactor support
tksupport.install(win)

# at this point build Tk app as usual using the root object,
# and start the program with "reactor.run()", and stop it
# with "reactor.stop()".

# Modified Button Click Function 
def clickMe():
    action.configure(text='Hello ' + name.get())

def click_open_webbrowser():
    if platform == 'darwin':
        webbrowser.get("open -a /Applications/Google\ Chrome.app %s").open_new_tab('http://127.0.0.1:8080/')
    elif platform == 'win32':
        webbrowser.get("chrome").open_new_tab('127.0.0.1:8080')

# Menu exit
def menu_quit():
    win.quit()
    win.destroy()
    reactor.stop()
    exit()

# Menu Build
def menu_build():
    menuBar = tk.Menu(win)
    win.config(menu=menuBar)
    fileMenu = tk.Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label="파일", menu=fileMenu)
    fileMenu.add_command(label="새파일")
    fileMenu.add_separator() # 4
    fileMenu.add_command(label="Exit", command=menu_quit)

    helpMenu = tk.Menu(menuBar, tearoff=0) # 6
    helpMenu.add_command(label="About")
    menuBar.add_cascade(label="Help", menu=helpMenu)

def on_closing():
    if messagebox.askokcancel("Quit", "프로그램을 끝내시겠습니까?"):
        menu_quit()

# Modify adding a Label 
aLabel = ttk.Label(win, text="이름:")
aLabel.grid(column=0, row=0, sticky='W')

# Adding a Textbox Entry widget
name = tk.StringVar()
nameEntered = ttk.Entry(win, width=12, textvariable=name)
nameEntered.grid(column=0, row=1, sticky='W')

ttk.Label(win, text="번호 선택:").grid(column=1, row=0, sticky='W')
number = tk.StringVar()
numberChosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')

numberChosen['values'] = (1, 2, 4, 42, 100) # 4
numberChosen.grid(column=1, row=1) # 5
numberChosen.current(0)

# Adding a Button 
action = ttk.Button(win, text="Click Me!", command=clickMe)
action.grid(column=2, row=1)

# Adding a Button 
btn_open_webbrowser = ttk.Button(win, text="Open Chrome", command=click_open_webbrowser)
btn_open_webbrowser.grid(column=0, row=2)

menu_build()

win.protocol("WM_DELETE_WINDOW", on_closing)

app = Klein()

@app.route('/')
def pg_root(request):
    return 'I am the root page!'

@app.route('/about')
def pg_about(request):
    return 'I am a Klein application!'

reactor.listenTCP(8080, Site(app.resource()))

reactor.run()


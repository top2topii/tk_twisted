# tksupport.py
from tkinter import simpledialog, messagebox
from twisted.internet import task

_task = None

def install(widget, ms=10, reactor=None):
    """Install a Tkinter.Tk() object into the reactor."""
    installTkFunctions()
    global _task
    _task = task.LoopingCall(widget.update)
    _task.start(ms / 1000.0, False)

def uninstall():
    """Remove the root Tk widget from the reactor.

    Call this before destroy()ing the root widget.
    """
    global _task
    _task.stop()
    _task = None

def installTkFunctions():
    import twisted.python.util
    twisted.python.util.getPassword = getPassword

def getPassword(prompt = '', confirm = 0):
    while 1:
        try1 = simpledialog.askstring('Password Dialog', prompt, show='*')
        if not confirm:
            return try1
        try2 = simpledialog.askstring('Password Dialog', 'Confirm Password', show='*')
        if try1 == try2:
            return try1
        else:
            messagebox.showerror('Password Mismatch', 'Passwords did not match, starting over')

__all__ = ["install", "uninstall"]
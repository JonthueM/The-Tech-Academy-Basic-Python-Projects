#!/user/bin/python
# -*- coding: utf-8 -*-

#
#   Python Ver: 3.8.2
#
#   Author:     Jonthue J. Michel
#
#   Purpose:    Assignment 122 Check File GUI using Grid
#
#   Tested OS:  This code was written and tested to work with Windows 10.

from tkinter import *
import tkinter as tk

import gui
import func


class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(450,220)
        self.master.maxsize(450,220)
        self.master.title("Check Files")
        self.master.configure(bg="lightgrey")
        root.columnconfigure(0, weight=1)
        root.columnconfigure(1, weight=1)
        root.columnconfigure(2, weight=1)
        

        gui.load_gui(self)
        




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()

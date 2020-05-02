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

def load_gui(self):
    #Browse Button 1 and 2
    self.btn_browseOne = tk.Button(self.master,width=13, height=2, text='Browse...')
    self.btn_browseOne.grid(row=2, column=0,padx=(1,0), pady=(20,10))
    self.btn_browseTwo = tk.Button(self.master,width=13, height=2, text='Browse...')
    self.btn_browseTwo.grid(row=3, column=0, padx=(1,0), pady=(20,10))
    #Entry Fields
    self.txt_browseEntryOne = tk.Entry(self.master,text='')
    self.txt_browseEntryOne.grid(row=2, column=1, rowspan=1, columnspan=3, padx=(10,30),pady=(20,10),sticky=NSEW)
    self.txt_browseEntryTwo = tk.Entry(self.master, text='')
    self.txt_browseEntryTwo.grid(row=3, column=1, rowspan=1, columnspan=3, padx=(10,30),pady=(20,10),sticky=NSEW)
    #Other Buttons
    self.btn_checkForFiles = tk.Button(self.master, width=13, height=2, text='Check for files...')
    self.btn_checkForFiles.grid(row=20, column=0, padx=(0,2), pady=(10,10))
    self.btn_closeProgram = tk.Button(self.master, width=12, height=2, text='Close Program')
    self.btn_closeProgram.grid(row=20, column=3, padx=(15,32), pady=(10,10))

if __name__ == "__main__":
    pass

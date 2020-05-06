from tkinter import filedialog
from tkinter import *
import tkinter as tk


import main
import gui


def getDir(self):
    getPath = filedialog.askdirectory()
    self.txt_browseEntryOne.delete(0,END)
    self.txt_browseEntryOne.insert(0,getPath)
    return getPath

def getDir2(self):
    getPath2 = filedialog.askdirectory()
    self.txt_browseEntryTwo.delete(0,END)
    self.txt_browseEntryTwo.insert(0,getPath2)
    return getPath2



    if __name__=="__main__":
        pass

        
        
    

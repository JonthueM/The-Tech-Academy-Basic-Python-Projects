from tkinter import filedialog
from tkinter import *
import tkinter as tk
import os, sys, time, time, shutil, sqlite3


import main
import gui

f = ''

'''
def create_db(self):
    conn = sqlite.connect('DestinationRecords')
    with conn:
        cur = conn.cursor()
        cur.execute('CREATE TABLE if not exists records(ID INTEGER PRIMARY KEY AUTOINCREMENT, col_fname TEXT, );')
        conn.commir()
        
 '''       


def getSource(self):
    source = filedialog.askdirectory()
    self.txt_getSource.delete(0,END)
    self.txt_getSource.insert(0,source)
    global sPath
    sPath = source
    print('You have picked {} as your source '.format(source))
    return  source



def getDestination(self):
    getDestinationPath = filedialog.askdirectory()
    self.txt_getDestination.delete(0,END)
    self.txt_getDestination.insert(0,getDestinationPath)
    global dPath
    dPath = getDestinationPath
    directorySource = os.listdir(getDestinationPath)
    print('You have picked {} as your path'.format(getDestinationPath))
    return  getDestinationPath

def testPrint1(self):
    os.listdir(selectedSourcePath)
    print(os.listdir(selectedSourcePath))


def Automatize(self):
    for f in os.listdir(sPath):
        if sPath.endswith(".txt"):
            shutil.move(f,dPath)
            print(f)
            
            

 
if __name__ == "__main__":
    pass

        
        
    

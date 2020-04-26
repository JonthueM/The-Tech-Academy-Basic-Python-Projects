# Importing os, time
import os
import time


#Simple Varible
procedingFolder = "101assignment"
Folder = 'C:\\PyProjects\\'
files = ""

#Combine & Sort
fullPath = os.path.join(Folder,procedingFolder)
time_modified = os.path.getmtime(fullPath) 
local_Time = time.ctime(time_modified)
directoryList = os.listdir(fullPath)




#Sort & Display

for files in directoryList: 
    if files.endswith(".txt"):
        print(files, local_Time)


    






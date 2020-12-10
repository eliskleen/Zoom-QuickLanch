import getpass
import os
import re
import time
import ctypes
from os.path import isfile, join



def getLines():
    settings = open(fileName)
    lines = settings.read().split("\n")
    return lines
def getNewProfile():
    currentDir = os.getcwd()
    file=open("profile.txt")
    lines = file.read().split("\n")
    # "icon": "C:\Chalmers\RoligaProjekt\ZoomOpen\Install\ZoomIconSmol.png",
    lines[8]= "                \"icon\": \"" + currentDir + "\\ZoomIconSmol.png\","
    lines[9] = "                \"backgroundImage\": \"" + currentDir + "\\Zoom_Icon.jpg\","
    lines[13] = "                \"startingDirectory\": \"" + currentDir + "\..\\" + "\","
    lines[8] = lines[8].replace("\\", "\\\\")
    lines[9] = lines[9].replace("\\", "\\\\")
    lines[13] = lines[13].replace("\\", "\\\\")
    print(lines[9])
    return lines


def getFullStr(ls):
    str = ""
    for i in range(len(ls)):
       str += (ls[i] + "\n" )
    return str

fileName = ""

if __name__ == "__main__":
    name = getpass.getuser()
    fileName = "C:\\Users\\" + name + "\\AppData\\Local\\Packages\\Microsoft.WindowsTerminal_8wekyb3d8bbwe\\LocalState\\settings.json"
    #fileName = "C:\\Chalmers\\RoligaProjekt\\ZoomOpen\\testSettings.txt"
    lines=getLines()
    top = []
    bottom=[]
    a=0
    lineToInsertOn =0
    listFound = False
    for line in lines:
        if(line.__contains__("\"list\":")):
            listFound = True
        if((listFound & line.__contains__("[")) or line.__contains__("\"list\": [")):
            lineToInsertOn = a+1
            break
        a +=1
    
    profile  = getNewProfile()
    newSettings = lines[:lineToInsertOn] + profile + lines[lineToInsertOn:]
    settings = open(fileName, 'w')
    settings.write(getFullStr(newSettings))

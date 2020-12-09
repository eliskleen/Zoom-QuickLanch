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
    lines[9]= "                \"icon\": \"" + currentDir + "\\ZoomIconSmol.png\","
    lines[10] = "                \"backgroundImage\": \"" + currentDir + "\\Zoom_Icon.jpg\","
    lines[14] = "                \"startingDirectory\": \"" + currentDir + "\..\\" + "\","
    lines[9] = lines[9].replace("\\", "\\\\")
    lines[10] = lines[10].replace("\\", "\\\\")
    lines[14] = lines[14].replace("\\", "\\\\")
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
    for line in lines:
        if(a<44):
            top.append(line)
        else:
            bottom.append(line)
        a +=1
    profile  = getNewProfile()

    newSettings = top + profile + bottom
    settings = open(fileName, 'w')
    settings.write(getFullStr(newSettings))

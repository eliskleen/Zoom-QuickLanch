from PIL import Image
import pyscreenshot as ImageGrab
import os
import re
import pyautogui
import time
import ctypes
import imagehash
from os.path import isfile, join



def getLink(line):
    return re.split(";", line, 1)[1]

def getLines():
    currentDir = os.getcwd() + "\\zoomLinks.txt"
    if(os.path.exists(currentDir)):
        file = open(currentDir, mode='r',encoding="utf-8")
        lines = file.read().split("\n")
        file.close()
        retLines = 0
        for l in lines:
            if not l.__contains__("h"):
                lines.remove(l)
        return lines
    else:
        file = open(currentDir, mode='w',encoding="utf-8")
        return []
def openZoomLink(linkAndPass):
    link = re.split(";", linkAndPass, 1)[0]
    os.system("start  "+ link)


def waitForZoom():
    currentDir = os.getcwd()
    reName = currentDir + "\\picture\\tmp\\current.png"
    promtName = currentDir + "\\picture\\prompt.png"
    while(1):
        currentScreen = ImageGrab.grab(bbox=(topX, topY, topX + sizeX, topY + sizeY))
        #Resize the screenshot to compare to prompt
        currentScreen.save(reName) 
        err=checkIfSame(reName, promtName)
        if(err<10):
            return
            
def checkIfSame(imgA, imgB):
    hash0 = imagehash.average_hash(Image.open(imgA)) 
    hash1 = imagehash.average_hash(Image.open(imgB)) 
    return (hash0 - hash1)

def tabToCorrectMeeting(passW):
    time.sleep(4)
    tabs = int(re.split(":", passW, 1)[1])
    for i in range(tabs):
        pyautogui.hotkey("tab")
        time.sleep(0.2)
    pyautogui.typewrite("\n")    
        


def enterPass(linkAndPass):
    passW = re.split(";", linkAndPass, 1)[1] 
    pyautogui.typewrite(list(passW + "\n"))

def closeWindowInChrome(numberOfTabs):
    pyautogui.hotkey("altleft", "tab")
    time.sleep(0.2)
    for i in range(numberOfTabs):
        pyautogui.hotkey("ctrlleft", "w")
        time.sleep(0.2)
    pyautogui.hotkey("altleft",  "tab")
    time.sleep(0.2)

def addNewLinkAndPass():
    print("Namn på den nya länken:")
    name = input()
    print("Skriv in den nya länken: ")
    link = input()
    print("Skriv in lösenordet")
    passW = input()
    fileName = os.getcwd() + "\\zoomLinks.txt"
    file = open(fileName, "a")
    file.write("\n" + name + ";" + link + ";" + passW)
    file.close()
    

def removeOldLink():
    print("Nummret på länken som ska bort:")
    numToRemove = int(input())
    lines = getLines()
    lines.pop(numToRemove -1)
    fileName = os.getcwd() + "\\zoomLinks.txt"
    file = open(fileName, "w")
    for i in range(len(lines)):
        file.write(lines[i])
        if(i < len(lines)-1):
            file.write("\n")
    file.close() 

scale = 1
sizeX = 0
sizeY = 0
topX = 0
topY = 0

if __name__ == "__main__":
    #Get the scale factor:
    scaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100
    #print(scaleFactor)
    scale=scaleFactor
    #rescale sizes
    sizeX = int(150*scale)
    sizeY = int(300*scale)
    #Get screen size and calculate where to screenshot
    user32 = ctypes.windll.user32
    [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    topX = int(w/2 - sizeX/2)
    topY = int(h/2 - sizeY/2)
    sizeY=int(150*scale)
    lines = getLines()
    a = 1
    for line in lines:
        if(line != ""):
            print(str(a) + ": " + re.split(";", line)[0])
            a += 1
    print("\na" + ": " "Lägg till ny länk och lösen")
    print("r" + ": " "Ta bort en länk och lösen")
    print("Välj nummret på de mötet du vill joina: ")
    while(1):
        answer = input()
        if answer == "a":
            addNewLinkAndPass()
            pyautogui.hotkey("ctrlleft", "shift", "1") 
            exit()
        elif answer == "r":
            removeOldLink()
            pyautogui.hotkey("ctrlleft", "shift", "1") 
            exit()
        elif answer == "q":
            break
        else:
            choosenLine = lines[int(answer)-1]
            linkAndPass = getLink(choosenLine)
            openZoomLink(linkAndPass)
            passW = re.split(";", linkAndPass, 1)[1] 
            if(re.split(":", passW, 1)[0]  == "tab"):
                tabToCorrectMeeting(passW)
                time.sleep(5)
                closeWindowInChrome(2)
            else:
                if(passW != ""):
                    waitForZoom()
                    closeWindowInChrome(1)
                    enterPass(linkAndPass)
                else:
                    tabToCorrectMeeting(":0")
                    closeWindowInChrome(1)
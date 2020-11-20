from PIL import Image
import pyscreenshot as ImageGrab
import os
import re
import pyautogui
import time
import ctypes

from os.path import isfile, join



def getLink(line):
    return re.split(";", line, 1)[1]

def getLines():
    currentDir = os.getcwd() + "\\zoomLinks.txt"
    file = open(currentDir, mode='r')
    lines = file.read().split("\n")
    return lines
def openZoomLink(linkAndPass):
    link = re.split(";", linkAndPass, 1)[0]
    os.system("start  "+ link)


def checkIfSame(imgA, imgB):
    pixA = imgA.convert('RGB')
    pixB = imgB.convert('RGB')
    err = 0
    for x in range(sizeX):
        for y in range(sizeY):
            (rX, gX, bX) = pixA.getpixel((x, y))
            (rY, gY, bY) = pixB.getpixel((x, y))
            currentErr = abs(rX-rY) + abs(gX - gY) + abs(bX - bY)

            err += currentErr

    return err


scale = 1
topX = int(764/scale)
topY = int(340/scale)
sizeX = int(200*scale)
sizeY = int(200*scale)





def waitForZoom():
    a = 0
    picFolder = os.getcwd() + "\\prompts"
    onlyfiles = os.listdir(picFolder)
    # print(onlyfiles)
    while 1:
        # time.sleep(1)
        a += 1
        currentScreen = ImageGrab.grab(bbox=(topX, topY, topX + sizeX, topY + sizeY))
        for file in onlyfiles:
            pic = Image.open(picFolder + "\\" + file) 
            rezized = pic.resize((sizeX, sizeY))
            err1 = checkIfSame(rezized, currentScreen)
            #err2 = checkIfSame(zoomPromptWLine, currentScreen)
            #currentScreen.save("latest" + str(a) + ".png")
            # print(err1)
            # print(err3)
            if err1 == 0:
                return
            
def tabToCorrectMeeting(passW):
    time.sleep(4)
    tabs = int(re.split(":", passW, 1)[1])
    for i in range(tabs):
        pyautogui.hotkey("tab")
        time.sleep(0.2)
    pyautogui.typewrite("\n")    
    a = 0
    while 1:
        a += 1
        currentScreen = ImageGrab.grab(bbox=(topX, topY, topX + sizeX, topY + sizeY))
        err1 = checkIfSame(waitingForZoomInChrome, currentScreen)
        err2 = checkIfSame(zoomConnecting, currentScreen) 
        currentScreen.save("latest" + str(a) + ".png")
        print (err2)
        if err1 != 0 and err2 > 1000:
            return


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


zoomPrompt = Image.open('C:\\Chalmers\\RoligaProjekt\\ZoomOpen\\zoomPromptSmall.png')
zoomPromptWLine = Image.open('C:\\Chalmers\\RoligaProjekt\\ZoomOpen\\zoomPromptWLine.png') 
waitingForZoomInChrome = Image.open('C:\\Chalmers\\RoligaProjekt\\ZoomOpen\\waitingForZoomInChrome.png') 
zoomConnecting = Image.open('C:\\Chalmers\\RoligaProjekt\\ZoomOpen\\zoomConnecting.png')  


def addCurrentPromptToFolder():
    picFolder = os.getcwd() + "\\prompts"
    onlyfiles = os.listdir(picFolder)
    currentScreen = ImageGrab.grab(bbox=(topX, topY, topX + sizeX, topY + sizeY))
    numberOfPictues = len(onlyfiles)
    currentScreen.save(os.getcwd() + "\\prompts\\prompt" + str(numberOfPictues+1) + ".png")
 

if __name__ == "__main__":
    user32 = ctypes.windll.user32
    user32.SetProcessDPIAware()
    [w, h] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
    topX = int(w/2 - sizeX/2)
    topY = int(h/2 - sizeY/2)
    lines = getLines()
    

    

    a = 1
    for line in lines:
        print(str(a) + ": " + re.split(";", line)[0])
        a += 1
    print("\na" + ": " "Lägg till ny länk och lösen")
    print("r" + ": " "Ta bort en länk och lösen")
    print("Välj nummret på de mötet du vill joina: ")
    while(1):
        answer = input()
        if answer == "a":
            addNewLinkAndPass()
        elif answer == "r":
            removeOldLink()
        elif answer == "c":
            time.sleep(2)
            addCurrentPromptToFolder()
            closeWindowInChrome(1)
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
                # print("waiting")
                if(passW != ""):
                    waitForZoom()
                    closeWindowInChrome(1)
                    enterPass(linkAndPass)
                else:
                    tabToCorrectMeeting(":0")
                    closeWindowInChrome(1)
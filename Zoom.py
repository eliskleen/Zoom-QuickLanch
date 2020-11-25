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


topX = 764
topY = 340
sizeX = 200
sizeY = 200

def waitForZoom():
    currentDir = os.getcwd() + "\\positionsOnScreen.txt"
    file = open(currentDir, mode='r')
    lines = file.read().split("\n")
    a=0
    while(1):
        a = a % (len(lines))
        currentLine=lines[a].split(";")
        #print(currentLine)
        left = int(currentLine[0])
        top = int(currentLine[1])
        width = int(currentLine[2])
        height = int(currentLine[3])
        currentScreen = ImageGrab.grab(bbox=(left, top, left + width, top + height)) 
        err = checkIfSame(meetingPasscode ,currentScreen , width, height) 
        if(a == 10):
            currentScreen.save()
        print(err)
        a += 1
        if err == 0:
            break
            
def checkIfSame(imgA, imgB, w, h):
    pixA = imgA.convert('RGB')
    pixB = imgB.convert('RGB')
    err = 0
    for x in range(w):
        for y in range(h):
            (rX, gX, bX) = pixA.getpixel((x, y))
            (rY, gY, bY) = pixB.getpixel((x, y))
            currentErr = abs(rX-rY) + abs(gX - gY) + abs(bX - bY)
            err += currentErr

    return err
def tabToCorrectMeeting(passW):
    time.sleep(4)
    tabs = int(re.split(":", passW, 1)[1])
    for i in range(tabs):
        pyautogui.hotkey("tab")
        time.sleep(0.2)
    pyautogui.typewrite("\n")    
    a = 0
    while 1:
        point = pyautogui.locateOnScreen(lanchMeeting, grayscale=True)
        print(point)
        if point != None or a >= 15:
            time.sleep(4)
            return
        a += 1

        


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


meetingPasscode = Image.open('C:\\Chalmers\\RoligaProjekt\\ZoomOpen\\prompts\\MeetingPasscode.png')
lanchMeeting = Image.open('C:\\Chalmers\\RoligaProjekt\\ZoomOpen\\prompts\\LanchMeeting.png') 

def addCurrentPromptToFolder():
    while(1):
        point = pyautogui.locateOnScreen(meetingPasscode, grayscale=True)
        print(point)
        if point != None:
            break
    file = open(os.getcwd() + "\\positionsOnScreen.txt", 'r')
    txt = file.read()
    txt += "\n " + str(point.left) +";"+ str(point.top) +";" + str(point.width) +";"+ str(point.height)
    file = open(os.getcwd() + "\\positionsOnScreen.txt", 'w')
    file.write(txt)
    
 

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
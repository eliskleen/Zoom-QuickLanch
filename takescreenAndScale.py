from PIL import Image
import pyscreenshot as ImageGrab
import os
import re
import pyautogui
import time
import ctypes
import numpy as np
from skimage.io import imread
from skimage.metrics import structural_similarity as ssim
from skimage.transform import resize
import imagehash




#Calculates how alike they are, the higher the value tme more "same they are"
def checkIfSame(imgA, imgB):
    hash0 = imagehash.average_hash(Image.open(imgA)) 
    hash1 = imagehash.average_hash(Image.open(imgB)) 
    return (hash0 - hash1)
    # if hash0 - hash1 < cutoff:
    #   print('images are similar')
    # else:
    #   print('images are not similar')

    # im1 = imread(imgA)
    # im1 = resize(im1, (256, 256))
    # im2 = imread(imgB)
    # im2 = resize(im2, (256, 256))
    # similarity = ssim(im1, im2, multichannel=True)
    # return similarity
    # img_a_pixels = Image.open(imgA).getdata()
    # img_b_pixels = Image.open(imgB).getdata()
    # img_a_array = np.array(img_a_pixels)
    # img_b_array = np.array(img_b_pixels)
    # difference = (img_a_array == img_b_array).sum()
    # return difference
#Scale 1 ger        202800
#Scale 1,25 ger:    192424
#Scale 1,50 get:    192423
#Scale 1,75 ger:    191192







def waitForZoom():
    currentDir = os.getcwd()
    reName = currentDir + "\\picture\\tmp\\current.png"
    promtName = currentDir + "\\picture\\prompt.png"
    while(1):
        currentScreen = ImageGrab.grab(bbox=(topX, topY, topX + sizeX, topY + sizeY))
        #Resize the screenshot to compare to prompt
        currentScreen.save(reName) 
        err=checkIfSame(reName, promtName)
        print(err) 
            #if err >=191192:
                #return
#Scale 1 ger        202800
#Scale 1,25 ger:    192424
#Scale 1,50 get:    192423
#Scale 1,75 ger:    191192

if __name__ == "__main__":
    #Get the scale factor:
    scaleFactor = ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100
    print(scaleFactor)
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
    waitForZoom()
    while(1):
        val = input()
        if(val =='p'):
            currentScreen = ImageGrab.grab(bbox=(topX, topY, topX + sizeX, topY + sizeY))
            while(1):
                pic = Image.open("testPrompt.png")
                currentScreen = ImageGrab.grab(bbox=(topX, topY, topX + sizeX, topY + sizeY))
                rezized = currentScreen.resize((338, 200))
                rezized.save("re.png")
                #currentScreen.save('current_screen.png')
                err=checkIfSame("re.png", "testPrompt.png")
                print(err)
                if err >=191192:
                   break
    
import pyscreenshot as ImageGrab
from PIL import Image
import time



def checkIfSame(imgA, imgB):
    sizeX = 395
    sizeY = 361
    pixA = imgA.load()
    pixB = imgB.load()
    pixXY = imgA.load()
    err = 0
    for x in range(sizeX):
        for y in range(sizeY):
            (rX, gX, bX) = pixA[x, y]
            (rY, gY, bY) = pixB[x, y]
            # print (pixA[x, y])
            # print (pixB[x, y])
            pixXY[x, y] = (abs(rX-rY) , abs(gX - gY) , abs(bX - bY))
            currentErr = abs(rX-rY) + abs(gX - gY) + abs(bX - bY)
            if currentErr > 200:
                err += currentErr 
                # print (pixA[x, y])
                # print (pixB[x, y])
                # print(err)
                # time.sleep(1)
    return err

if __name__ == "__main__":
    sizeX = 395
    sizeY = 361
    topX = 764
    topY = 336
    while 1:
        currentScreen = ImageGrab.grab(bbox=(topX, topY, topX + 395, topY + 361)) # X1,Y1,X2,Y2
        pix = currentScreen.load()
        zoomPrompt = Image.open('C:\\Chalmers\\RoligaProjekt\\ZoomOpen\\zoomPrompt.jpg')
        # currentScreen.show()
        zoomPrompt.show()
        print(checkIfSame(currentScreen, zoomPrompt))
        break






#     from PIL import Image

# im = Image.open('dead_parrot.jpg') # Can be many different formats.
# pix = im.load()
# print im.size  # Get the width and hight of the image for iterating over
# print pix[x,y]  # Get the RGBA Value of the a pixel of an image
# pix[x,y] = value  # Set the RGBA Value of the image (tuple)
# im.save('alive_parrot.png')  # Save the modified pixels as .png
# Rename this file to be "filters.py"
# Add commands to import modules here.
from PIL import Image
# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(picName):
    im = Image.open(picName, mode='r')
    return im
# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(myPic):
    myPic.show()

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(pic0, filename):
    pic0.save(filename, format=None)

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(pic1):
    darkBlue = (0, 51, 76)
    red = (217, 26, 33)
    lightBlue = (112, 150, 158)
    yellow = (252, 227, 166)

    pixels = list(pic1.getdata())

    newImg = []

    for i in pixels:
        intensity = i[0] + i[1] + i[2]
        if intensity < 182:
            newImg.append(darkBlue)
        elif intensity >= 182 and intensity < 364:
            newImg.append(red)
        elif intensity >= 364 and intensity < 564:
            newImg.append(lightBlue)
        elif intensity >= 564:
            newImg.append(yellow)

    newImage = Image.new("RGB", (1024, 576), i)
    newImage.putdata(newImg)
    return newImage

def inverted(pic1):
    pixels = list(pic1.getdata())

    newImg = []

    for i in pixels:
        inverted = (255-i[0], 255-i[1], 255-i[2])
        newImg.append(inverted)

    newImage = Image.new("RGB", (1024, 576), i)
    newImage.putdata(newImg)
    return newImage

def grayscale(pic1):
    pixels = list(pic1.getdata())

    newImg = []

    for i in pixels:
        grayscale = (int(i[0]+i[1]+i[2])/3, int(i[0]+i[1]+i[2])/3, int(i[0]+i[1]+i[2])/3)
        newImg.append(grayscale)

    newImage = Image.new("RGB", (1024, 576), i)
    newImage.putdata(newImg)
    return newImage

def grayscaleInvert(pic1):
    pixels = list(pic1.getdata())

    newImg = []

    length = pixels.length()

    width = 1024
    height = 576

    for i in 0<(length/2):
        grayscale = (int(i[0]+i[1]+i[2])/3, int(i[0]+i[1]+i[2])/3, int(i[0]+i[1]+i[2])/3)
        newImg.append(grayscale)

    for i in (length/2) <= length:
        inverted = (255-i[0], 255-i[1], 255-i[2])
        newImg.append(inverted)

    newImage = Image.new("RGB", (1024, 576), i)
    newImage.putdata(newImg)
    return newImage

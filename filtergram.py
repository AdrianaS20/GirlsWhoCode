from filters import *

print("Welcome to Filtergram!")
picChoice = input("Which picture would you like to put a filter on?")

#Load image
Image = load_img(picChoice)

#Asks user to pick a filter
print("Which filter would you like to apply to this picture?")
filter = input("You can choose from obamicon, inverted, or grayscale.")

if filter == "obamicon":
    newImage = obamicon(Image)
    show_img(newImage)

elif filter == "inverted":
    newImage = inverted(Image)
    show_img(newImage)

elif filter == "grayscale":
    newImage = grayscale(Image)
    show_img(newImage)

elif filter == "grayscaleInvert":
    newImage = grayscaleInvert(Image)
    show_img(newImage)

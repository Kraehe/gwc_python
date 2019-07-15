# Rename this file to be "filters.py"
# Add commands to import modules here.
from PIL import Image


# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    image = Image.open(filename)
    return image
# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(image):
    image.show()


# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(image, filename):
    image.save(filename)

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(img):

    # gets the data of the image
    pixels = img.getdata()

    # make an empty list for the filtered pixels to be stored in
    newPixels = []
    #  tuples used to change the image
    darkBlue = (0,51,76)
    red = (217,26,33)
    lightBlue = (112,150,158)
    yellow = (252, 227,166)

    # loops through the pixels
    for p in pixels:
        # adds the rgb values together to determine the intensity
        intensity = p[0] + p[1] + p[2]
        # checks the intensity of each pixel and changes the color according to its intensity
        if intensity < 182:
            newPixels.append(darkBlue)
        elif intensity < 364:
            newPixels.append(red)
        elif intensity < 546:
            newPixels.append(lightBlue)
        else:
            newPixels.append(yellow)

    newMode = img.mode
    newSize = img.size
    newImg = Image.new(newMode, newSize)
    newImg.putdata(newPixels)
    return newImg


def softpink(img):
    pixels = img.getdata()
    newPixels = []

    nottoosoft = (255, 65, 65)
    kindasoft = (255, 88, 88)
    soft = (255, 132, 132)
    softer = (255, 179, 179)
    evensofter = (255, 196, 196)
    softest = (255, 208, 208)
    softestest = (255, 242, 242)

    for p in pixels:
        # adds the rgb values together to determine the intensity
        intensity = p[0] + p[1] + p[2]
        # checks the intensity of each pixel and changes the color according to its intensity
        if intensity < 50:
            newPixels.append(nottoosoft)
        elif intensity < 100:
            newPixels.append(kindasoft)
        elif intensity < 160:
            newPixels.append(soft)
        elif intensity < 350:
            newPixels.append(softer)
        elif intensity < 500:
            newPixels.append(evensofter)
        elif intensity < 700:
            newPixels.append(softest)
        else:
            newPixels.append(softestest)

    newMode = img.mode
    newSize = img.size
    newImg = Image.new(newMode, newSize)
    newImg.putdata(newPixels)
    return newImg

def synthwave():
    #asaaafdkjafnldnskd
    return

image = load_img("obama.jpg")
hawks = load_img("hawks.jpg")
spange = load_img("spange.jpg")
flowers = load_img("helianthus-yellow-flower-pixabay_11863.jpg")
new1 = obamicon(image)
new2 = softpink(hawks)
hell = obamicon(spange)
flowersss = softpink(flowers)
show_img(new1)
show_img(new2)
show_img(hell)
show_img(flowersss)
save_img(new1,"picture.jpg")
save_img(new2,"picture1.jpg")
save_img(hell,"picture2.jpg")

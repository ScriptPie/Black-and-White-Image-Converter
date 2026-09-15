from PIL import Image, ImageDraw

def ConvertImage(image):
    for i in range(imgHeight):
        for k in range(imgWidth):
            colorR, colorG, colorB = image.getpixel((k, i))          
            newColorY = int(round(0.299 * colorR + 0.587 * colorG + 0.114 * colorB))
            newColor = (newColorY, newColorY, newColorY)
            image.putpixel((k, i), newColor)
    return image

start_image = Image.open("start_images/start_image.jpg") # file name and directory what do you want to convert

imgWidth, imgHeight = start_image.size

if __name__ == "__main__":
    start_image = ConvertImage(start_image)
    start_image.save("end_images/end_image.jpg") # file name of converted image

from simpleimage import *
def reflect(filename):
    img = SimpleImage(filename)
    height = img.height
    width = img.width
    new_img = SimpleImage.blank(width, height * 2, "white")
    for y in range(height):
        for x in range(width):
            pixel = img.get_pixel(x, y)
            new_img.set_pixel(x, y, pixel)
            new_img.set_pixel(x, new_img.height - y - 1, pixel)
    new_img.show()
    
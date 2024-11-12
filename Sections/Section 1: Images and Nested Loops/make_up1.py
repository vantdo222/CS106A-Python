from simpleimage import *
def make_up1(filename):
    img = SimpleImage(filename)
    height = img.height
    width = img.width
    new_img = SimpleImage.blank(width * 2, height, 'white')
    for y in range(height):
        for x in range(width):
            pixel = img.get_pixel(x, y)
            new_img.set_pixel(x + (new_img.width - width) / 2, height - y - 1, pixel)
    new_img.show()
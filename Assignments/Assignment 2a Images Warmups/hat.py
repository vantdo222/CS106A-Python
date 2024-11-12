from simpleimage import *
def hat(filename, hat_height):
    img = SimpleImage(filename)
    height = img.height
    width = img.width
    new_img = SimpleImage.blank(width, height + hat_height, 'red')
    for pixel in new_img:
        pixel.green = 255
    for y in range(height):
        for x in range(width):
            pixel = img.get_pixel(x, y)
            new_img.set_pixel(x, y + hat_height, pixel)
    new_img.show()
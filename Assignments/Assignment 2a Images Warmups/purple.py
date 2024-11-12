from simpleimage import *
def purple(filename, bars_width):
    img = SimpleImage(filename)
    height = img.height
    width = img.width
    new_img = SimpleImage.blank(width + bars_width * 2, height, 'red')
    for pixel in new_img:
        pixel.blue = 255
    for y in range(height):
        for x in range(width):
            pixel = img.get_pixel(x, y)
            new_img.set_pixel(x + bars_width, y, pixel)
    new_img.show()
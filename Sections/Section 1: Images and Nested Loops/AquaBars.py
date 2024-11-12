from simpleimage import *
def aqua_bars(filename, bar_height):
    img = SimpleImage(filename)
    height = img.height
    width = img.width
    new_img = SimpleImage.blank(width, height + bar_height * 2, 'blue')
    for pixel in new_img:
        pixel.green = 255
    for y in range(height):
        for x in range(width):
            pixel = img.get_pixel(x, y)
            new_img.set_pixel(x, y + (new_img.height - height) / 2, pixel)
    new_img.show()
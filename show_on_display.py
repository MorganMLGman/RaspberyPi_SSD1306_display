from time import sleep

from Adafruit_SSD1306 import SSD1306_128_64 as driver
from PIL import Image, ImageDraw, ImageFont

display = driver(rst=None)

display.begin()
display.clear()
display.display()

height = display.height
width = display.width

screen = Image.new('1', (width, height))
draw = ImageDraw.Draw(screen)
draw.rectangle((0, 0, width, height), outline = 0, fill = 0)

font = ImageFont.load_default()
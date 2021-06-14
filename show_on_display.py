from time import sleep

from Adafruit_SSD1306 import SSD1306_128_64 as driver
from PIL import Image, ImageDraw, ImageFont

import get_sys_info 

display = driver(rst=None)

display.begin()
display.clear()
display.display()

height = display.height
width = display.width

screen = Image.new('1', (width, height))
draw = ImageDraw.Draw(screen)

font = ImageFont.truetype("fonts/OpenSans-Semibold.ttf", 12)

is_linux = get_sys_info.check_system_type('Linux')

while is_linux:    
    draw.rectangle((0, 0, width, height), outline = 0, fill = 0)
    draw.text((0, -2), get_sys_info.get_time(), font=font, fill = 255)

    
    display.image(screen)
    display.display()
    sleep(1)
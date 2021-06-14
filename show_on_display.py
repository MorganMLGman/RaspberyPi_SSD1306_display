from time import clock, sleep

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

font_clock = ImageFont.truetype("fonts/OpenSans/OpenSans-Semibold.ttf", 18)
font_clock_offset_v = int(font_clock.getsize('0')[1] * -0.25)
font_clock_size = (font_clock.getsize('0')[0], font_clock.getsize('0')[1] - font_clock_offset_v)

font_data = ImageFont.truetype("fonts/OpenSans/OpenSans-Semibold.ttf", 12)
font_data_offset_v = int(font_data.getsize('0')[1] * -0.25)
font_data_size = (font_data.getsize('0')[0], font_data.getsize('0')[1] - font_data_offset_v)

print( font_data.getsize("O"))

is_linux = get_sys_info.check_system_type('Linux')

def update_clock() -> Image:
    info = get_sys_info.get_time()
    clock = Image.new('1', (width, font_clock_size[1]))
    clock_draw = ImageDraw.Draw(clock)
    clock_draw.rectangle((0, 0, width, font_clock_size[1]), outline = 0, fill = 0)
    length = 0
    for letter in info:
        length += font_clock.getsize(letter)[0]
    clock_draw.text(((width - length)/2, font_clock_offset_v), info, font=font_clock, fill = 255)
    return clock

def update_data(function) -> Image:
    data = Image.new('1', (width, font_data_size[1]))
    data_draw = ImageDraw.Draw(data)
    data_draw.rectangle((0, 0, width, font_data_size[1]), outline = 0, fill = 0)
    data_draw.text((0, font_data_offset_v), function(), font = font_data, fill = 255)
    return data

while is_linux:
    clock_screen = update_clock();
    data_screen = update_data(get_sys_info.get_cpu_usage)
    screen.paste(clock_screen, (0, 0))
    screen.paste(data_screen, (0, clock_screen.size[1] + font_clock_offset_v))
    display.image(screen)
    display.display()
    sleep(1)
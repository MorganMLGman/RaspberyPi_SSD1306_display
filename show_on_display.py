from time import sleep, time
from datetime import datetime
from sched import scheduler
from Adafruit_SSD1306 import SSD1306_128_64 as driver
from PIL import Image, ImageDraw, ImageFont
import get_sys_info 

def microseconds():
    return (time() * 1000000 + datetime.now().microsecond)

def sleep_timer(time: float) -> None:
    sleep(time/999999)

timer = scheduler(microseconds, sleep_timer)

display = driver(rst=None)

display.begin()
display.clear()
display.display()

height = display.height
width = display.width



screen = Image.new('1', (width, height))
screen_draw = ImageDraw.Draw(screen)

font_clock = ImageFont.truetype("fonts/OpenSans/OpenSans-Bold.ttf", 18)
font_clock_offset_v = int(font_clock.getsize('0')[1] * -0.25)
font_clock_size = (font_clock.getsize('0')[0], font_clock.getsize('0')[1] - font_clock_offset_v)

font_data = ImageFont.load_default()
font_data_offset_v = int(font_data.getsize('0')[1] * -0.25)
font_data_size = (font_data.getsize('0')[0], font_data.getsize('0')[1] - font_data_offset_v)

is_linux = get_sys_info.check_system_type('Linux')

def update_clock() -> Image:
    info = get_sys_info.get_time()
    clock = Image.new('1', (width, font_clock_size[1]))
    clock_draw = ImageDraw.Draw(clock)
    # clock_draw.rectangle((0, 0, width, font_clock_size[1]), outline = 0, fill = 0)
    length = 0
    for letter in info:
        length += font_clock.getsize(letter)[0]
    clock_draw.text(((width - length)/2, font_clock_offset_v), info, font=font_clock, fill = 255)
    return clock

def update_data(function) -> Image:
    info = function()
    length = 0
    for letter in info:
        length += font_data.getsize(letter)[0]
    
    data = Image.new('1', (length, font_data_size[1]))
    data_draw = ImageDraw.Draw(data)
    data_draw.text((0, font_data_offset_v), info, font = font_data, fill = 255)
    return data


def update_screen(sc):
    screen_draw.rectangle((0, 0, width, height), outline = 0, fill = 0)
    clock_screen = update_clock();
    cpu_screen = update_data(get_sys_info.get_cpu_usage)
    ip_screen = update_data(get_sys_info.get_ip_address)
    ram_screen = update_data(get_sys_info.get_ram_usage)
    disk_screen = update_data(get_sys_info.get_disk_usage)
    temp_screen = update_data(get_sys_info.get_temperature)
    screen.paste(clock_screen, (0, 0))
    screen.paste(cpu_screen, (0, clock_screen.size[1] + font_clock_offset_v - 1))
    screen.paste(ram_screen, (cpu_screen.size[0] + 5, clock_screen.size[1] + font_clock_offset_v - 1))
    screen.paste(ip_screen, (0,  clock_screen.size[1] + cpu_screen.size[1] + font_data_offset_v + font_clock_offset_v - 1))
    screen.paste(disk_screen, (0,  clock_screen.size[1] + cpu_screen.size[1] * 2 + font_data_offset_v * 2 + font_clock_offset_v - 1))
    screen.paste(temp_screen, (0,  clock_screen.size[1] + cpu_screen.size[1] * 3 + font_data_offset_v * 3 + font_clock_offset_v - 1))
    display.image(screen)
    display.display()
    timer.enter(500000, 1, update_screen, (timer,))

if is_linux:
    timer.enter(500000, 1, update_screen, (timer,))
    timer.run()
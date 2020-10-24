#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

if __name__ == "__main__":
    RST = None     # on the PiOLED this pin isnt used
    DC = 23
    SPI_PORT = 0
    SPI_DEVICE = 0
    
    disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)
    disp.begin()
    
    disp.clear()
    disp.display()
    
    width = disp.width
    height = disp.height
    image = Image.new('1', (width, height))
    
    draw = ImageDraw.Draw(image)
    
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    
    padding = -2
    top = padding
    bottom = height-padding
    x = 0
    
    font = ImageFont.load_default()
    
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    cmd = "systemctl status netapp.service | grep -o 'http.*'"
    DOMAIN = subprocess.check_output(cmd, shell = True )
    
    draw.text((x, top), DOMAIN, font=font, fill=255)
    
    disp.image(image)
    disp.display()
    time.sleep(.1)

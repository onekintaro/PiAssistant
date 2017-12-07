# coding: utf8
import os
import logging
import subprocess
import sys
import urllib

import time
import math
from random import randrange



# Import library
import multilineMAX7219 as LEDMatrix
# Import fonts
from multilineMAX7219_fonts import CP437_FONT, SINCLAIRS_FONT, LCD_FONT, TINY_FONT

# The following imported variables make it easier to feed parameters to the library functions
from multilineMAX7219 import DIR_L, DIR_R, DIR_U, DIR_D
from multilineMAX7219 import DIR_LU, DIR_RU, DIR_LD, DIR_RD
from multilineMAX7219 import DISSOLVE, GFX_ON, GFX_OFF, GFX_INVERT

import RPi.GPIO as GPIO

def say(words):
    stream = "/home/pi/speech.sh " + words
    os.system(stream)

# Initialise the library and the MAX7219/8x8LED arrays
LEDMatrix.init()

try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(26,GPIO.OUT)
    GPIO.setup(6,GPIO.OUT)
    
    P1 = [[0,0,0,0,0,0,0,0],
          [1,1,1,1,1,1,1,1],
          [1,0,0,0,0,0,0,0],
          [1,0,0,0,0,0,0,0],
          [0,1,0,0,0,0,0,0],
          [0,0,1,0,0,0,0,0],
          [0,0,0,1,1,1,1,1],
          [0,0,0,0,0,0,0,0]]
    P2 = [[0,0,0,0,0,0,0,0],
          [1,1,1,1,1,1,1,1],
          [0,0,0,0,0,0,0,1],
          [0,0,0,0,0,0,0,1],
          [0,0,0,0,0,0,1,0],
          [0,0,0,0,0,1,0,0],
          [1,1,1,1,1,0,0,0],
          [0,0,0,0,0,0,0,0]]
    LEDMatrix.gfx_set_all(GFX_OFF)
    LEDMatrix.gfx_sprite_array(P1, 0,0)
    LEDMatrix.gfx_sprite_array(P2, 0,8)
    LEDMatrix.gfx_render()
    GPIO.output(26,GPIO.HIGH)
    GPIO.output(6,GPIO.HIGH)
    say("Hallo, ich bin ein Prototyp.") 
    time.sleep(1)
    P1 = [[0,0,0,0,0,0,1,1],
          [0,0,0,0,0,1,0,0],
          [0,0,0,0,1,0,0,0],
          [0,0,0,0,1,0,0,0],
          [0,0,0,0,1,0,0,0],
          [0,0,0,0,0,1,0,0],
          [0,0,0,0,0,0,1,1],
          [0,0,0,0,0,0,0,0]]
    P2 = [[1,1,0,0,0,0,0,0],
          [0,0,1,0,0,0,0,0],
          [0,0,0,1,0,0,0,0],
          [0,0,0,1,0,0,0,0],
          [0,0,0,1,0,0,0,0],
          [0,0,1,0,0,0,0,0],
          [1,1,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0]]
    LEDMatrix.gfx_set_all(GFX_OFF)
    LEDMatrix.gfx_sprite_array(P1, 0,0)
    LEDMatrix.gfx_sprite_array(P2, 0,8)
    LEDMatrix.gfx_render()
    say("Tschüss.") 
    time.sleep(1)
    LEDMatrix.clear_all()
    GPIO.output(26,GPIO.LOW)
    GPIO.output(6,GPIO.LOW)
	
except KeyboardInterrupt:
    # reset array
    LEDMatrix.scroll_message_horiz(["","Goodbye!",""], 1, 8)
    LEDMatrix.clear_all()
    GPIO.output(26,GPIO.LOW)
    GPIO.output(6,GPIO.LOW)
    
	
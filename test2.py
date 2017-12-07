#!/usr/bin/env python
# ---------------------------------------------------------
# Filename: multilineMAX7219_demo.py
# ---------------------------------------------------------
# Demonstration of the features in the multilineMAX7219 library
#
# v1.0
# F.Stern 2014
# ---------------------------------------------------------
# improved and extended version of JonA1961's MAX7219array
# ( https://github.com/JonA1961/MAX7219array )
# ---------------------------------------------------------
# See multilineMAX7219.py library file for more details
# ---------------------------------------------------------
# This demo script is intended to run on an array of 9 (3x3)
#   MAX7219 boards, connected as described in the library
#   script. 
# The variables MATRIX_WIDTH and MATRIX_HEIGHT, defined in the 
#	multilineMAX7219.py library script, should always be set to be 
#	consistent with the actual hardware setup in use.  If it is 
#	not set correctly, then the functions will not work as
#   intended
# ---------------------------------------------------------
import logging
import subprocess
import sys

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
    for loop in range(4):
        for brightness in range(15*(loop%2), 16-17*(loop%2), 1-2*(loop%2)):
            LEDMatrix.brightness(brightness)
            time.sleep(0.1)
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
    
	
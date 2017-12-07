import sys
import time
import datetime
import RPi.GPIO as GPIO
import tm1637
 
Display = tm1637.TM1637(15,14,tm1637.BRIGHT_TYPICAL)
 
Display.Clear()
Display.SetBrightnes(1)
 
while(True):
   now = datetime.datetime.now()
   hour = now.hour
   minute = now.minute
   second = now.second
   currenttime = [ int(hour / 10), hour % 10, int(minute / 10), minute % 10 ]
 
   Display.Show(currenttime)
   Display.ShowDoublepoint(second % 2)
 
   time.sleep(1)
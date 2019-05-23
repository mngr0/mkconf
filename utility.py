import hal
import linuxcnc
import time
import tclab


class utility:
  def __init__(self,name="utility"):
    self.h= hal.component(name)
    self.h.newpin("home-all",hal.HAL_BIT, hal.HAL_IN)
    self.h.newpin("pause",hal.HAL_BIT, hal.HAL_IN)
    self.h.newpin("convert-gcode",hal_BIT, hal.HAL_OUT)
    self.old_home = 0;
    self.old_convert = 0;
    self.pause = 0;

  def routine (self):
    if self.old_home == 0 and self.h["home-all"]==1:
      print ("must home!")
    self.old_home = self.h["home_all"]

    if self.pause == 0 and self.h["pause"]==1:
      print ("must pause!")
    self.old_home = self.h["pause"]

    if self.convert == 0 and self.h["convert-gcode"]==1:
      print ("must convert!")
    self.old_convert = self.h["convert_gcode"]


comp = utility()
try:
  while 1:
    comp.routine()
    time.sleep(0.3)

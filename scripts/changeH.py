#!/usr/bin/python

from machinekit import hal
import linuxcnc
import sys

cmd=linuxcnc.command()
stat=linuxcnc.stat()

stat.poll()
H=stat.actual_position[2]

def output_ini(path,home,offset):
  #path="test" #read from machinekit.ini
  f=open(path,"w+")
  f.write("""
[EMC]
VERSION =               $Revision$
MACHINE =               bianca
DEBUG = 0

[DISPLAY]
DISPLAY =               axis
CYCLE_TIME =            0.200
HELP_FILE =             tklinucnc.txt
POSITION_OFFSET =       RELATIVE
POSITION_FEEDBACK =     ACTUAL
MAX_FEED_OVERRIDE =     1.2
PROGRAM_PREFIX = /home/machinekit/Documents/gh/mkconf/scripts
INTRO_GRAPHIC =         machinekit.gif
INTRO_TIME =            5
EDITOR = gedit
PYVCP = 3D.Temps.panel.xml

[TASK]
TASK =                  milltask
CYCLE_TIME =            0.010

[RS274NGC]
PARAMETER_FILE =        stepper.var
SUBROUTINE_PATH = /home/machinekit/Documents/gh/mkconf/scripts

[EMCMOT]
EMCMOT =                motmod
COMM_TIMEOUT =          1.0
COMM_WAIT =             0.010
BASE_PERIOD =           50000
SERVO_PERIOD =          1000000

[HAL]
HALUI   =               halui
HALFILE =               core_stepper.hal
HALFILE =               standard_pinout.hal
HALFILE =               temp.hal
POSTGUI_HALFILE = 3D.postgui.hal

[TRAJ]
AXES =                  4
COORDINATES =           X Y Z A
HOME =                  0 0 0 0
LINEAR_UNITS =          mm
ANGULAR_UNITS =         degree
CYCLE_TIME =            0.010
DEFAULT_VELOCITY =      0.0167
MAX_VELOCITY =          500
DEFAULT_ACCELERATION =  300.0
MAX_ACCELERATION =      350.0
  """)
  for i in range(3):
    f.write("""
[AXIS_%s]
TYPE =                          LINEAR
MAX_VELOCITY =                  50
MAX_ACCELERATION =              1000.0
STEPGEN_MAXACCEL =              7001.0
BACKLASH =                      0.000
SCALE =                         82.15
OUTPUT_SCALE =                  1.000
MIN_LIMIT =                     -1000.0
MAX_LIMIT =                     1500.0
FERROR =                        0.050
MIN_FERROR =                    0.010
HOME =                          %s
HOME_OFFSET =                   %s
HOME_SEARCH_VEL =               -20.0
HOME_LATCH_VEL =                1.0
HOME_USE_INDEX =                NO
HOME_IGNORE_LIMITS =            YES
HOME_FINAL_VEL =                1.0
"""%(i,home,offset))
  f.write("""
[AXIS_3]
TYPE =                          ANGULAR
HOME =                          0.000
MAX_VELOCITY =                  50
MAX_ACCELERATION =              1000.0
STEPGEN_MAXACCEL =              7001.0
BACKLASH =                      0.000
SCALE =                         145.6
OUTPUT_SCALE =                  1.000
MIN_LIMIT =                     -99999999
MAX_LIMIT =                     999999999.0
FERROR =                        0.050
MIN_FERROR =                    0.010
HOME_OFFSET =                   0.0
HOME_SEARCH_VEL =               0.0
HOME_LATCH_VEL =                0.0
HOME_USE_INDEX =                NO
HOME_IGNORE_LIMITS =            NO

[EMCIO]

EMCIO =                 io
CYCLE_TIME =            0.100
TOOL_TABLE = stepper.tbl
""")

home=range(3)
homeoffset=range(3)

for i in range(3):
  home[i]= hal.Pin("axis.%s.home" %str(i))
  homeoffset[i]= hal.Pin("axis.%s.home-offset" %str(i))




def create_fun(type,value,Hlabel):
  if(type=="+"):
    def fun():
#      for i in range(3):
#        home[i].set(home[i].get()-value)
#        homeoffset[i].set(homeoffset[i].get()-value)
      cmd.mdi("G0 Z"+str(float(H)+value ))
      Hlabel.set(home[0].get())
  else:
    def fun():
#      for i in range(3):
#        home[i].set(home[i].get()+value)
#        homeoffset[i].set(homeoffset[i].get()+value)
      cmd.mdi("G0 Z"+str(float(H)+value ))
      Hlabel.set(home[0].get())
  return fun

from Tkinter import *
window = Tk()
window.title("cambiare altezza")
window.geometry("400x400")

lbl= Label(window, text="altezza attuale=")
lbl.grid(column=0, row=0)

Htext=StringVar(value=H)
#home[0].get()
altezza=Label(window, textvariable=Htext)
altezza.grid(column=1,row=0)
type=["+","-"]
amount=[.1,1,10]

for i,t in enumerate(type):
  for j,a in enumerate(amount):
    f=create_fun(str(t),a,Htext)
    b= Button(window,text=t+str(a),command=f)
    b.grid(column=2+j,row=i)
#btn conferma, sali 1,10,100

sethome=Button(window,text="imposta come 0")
sethome.grid(column=0,row=4)

s= Button(window,text="salva",command=output_ini(str(sys.argv[1]),home[0].get(),homeoffset[0].get() ) )
s.grid(column=1,row=4)
window.mainloop()

#!/usr/bin/python

from machinekit import hal

import sys

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

for i in range(3):
  print("axis"+str(i))
  print(home[i].get())
  print(homeoffset[i].get())

change=3
while 1:
  print("menu:\n\t1)sali\n\t2)scendi\n\t3)salva\n")
  opt=raw_input()
  try:
    opt=int(opt)
  except:
    print("comando non valido")
    sys.exit(0)
  if opt==1 or opt==2:
    print("quanto:")
    change=raw_input() #rimpiazzare , con .
    try:
      change=float(change)
      if opt == 2:
        change=-change
    except:
      print("valore non riconosciuto")
      exit(0)
    for i in range(3):
      home[i].set(home[i].get()-change)
      homeoffset[i].set(homeoffset[i].get()-change)
  if opt==3:
    if len(sys.argv) != 2:
      print ("to save, you must give an argument")
    if (not str(sys.argv[1]).endswith(".ini") ):
      print ("invalid file, it must ends with .ini")
    output_ini(str(sys.argv[1]),home[0].get(),homeoffset[0].get())

#salvare

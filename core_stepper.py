import os

from machinekit import hal
from machinekit import rtapi as rt
from machinekit import config as c

from fdm.config import motion


rt.init_RTAPI()
c.load_ini(os.environ['INI_FILE_NAME'])
motion.setup_motion(kinematics="lineardeltakins")
rt.loadrt("stepgen",step_type="0,0,0,0")
rt.loadrt("debounce")
#rt.newthread(name="base-thread", period=10000,instance=1)
"""
loadrt motmod base_period_nsec=50000 servo_period_nsec=1000000 num_joints=[TRAJ]AXES tp=tp kins=lineardeltakins
# hook functions to base thread (high speed thread for step generation)
addf stepgen.make-pulses base-thread

# hook functions to servo thread
addf stepgen.capture-position servo-thread
addf motion-command-handler servo-thread
addf motion-controller servo-thread
addf stepgen.update-freq servo-thread
addf debounce.0.funct servo-thread

# connect position commands from motion module to step generator
net Xpos-cmd axis.0.motor-pos-cmd => stepgen.0.position-cmd
net Ypos-cmd axis.1.motor-pos-cmd => stepgen.1.position-cmd
net Zpos-cmd axis.2.motor-pos-cmd => stepgen.2.position-cmd
net Apos-cmd axis.3.motor-pos-cmd => stepgen.3.position-cmd

# connect position feedback from step generators
# to motion module
net Xpos-fb stepgen.0.position-fb => axis.0.motor-pos-fb
net Ypos-fb stepgen.1.position-fb => axis.1.motor-pos-fb
net Zpos-fb stepgen.2.position-fb => axis.2.motor-pos-fb
net Apos-fb stepgen.3.position-fb => axis.3.motor-pos-fb

# connect enable signals for step generators
net Xen axis.0.amp-enable-out => stepgen.0.enable
net Yen axis.1.amp-enable-out => stepgen.1.enable
net Zen axis.2.amp-enable-out => stepgen.2.enable
net Aen axis.3.amp-enable-out => stepgen.3.enable

# connect signals to step pulse generator outputs
net Xstep <= stepgen.0.step
net Xdir  <= stepgen.0.dir
net Ystep <= stepgen.1.step
net Ydir  <= stepgen.1.dir
net Zstep <= stepgen.2.step
net Zdir  <= stepgen.2.dir
net Astep <= stepgen.3.step
net Adir  <= stepgen.3.dir

# set stepgen module scaling - get values from ini file
setp stepgen.0.position-scale [AXIS_0]SCALE
setp stepgen.1.position-scale [AXIS_1]SCALE
setp stepgen.2.position-scale [AXIS_2]SCALE
setp stepgen.3.position-scale [AXIS_3]SCALE

# set stepgen module accel limits - get values from ini file
setp stepgen.0.maxaccel [AXIS_0]STEPGEN_MAXACCEL
setp stepgen.1.maxaccel [AXIS_1]STEPGEN_MAXACCEL
setp stepgen.2.maxaccel [AXIS_2]STEPGEN_MAXACCEL
setp stepgen.3.maxaccel [AXIS_3]STEPGEN_MAXACCEL

"""

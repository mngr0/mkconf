from machinekit import hal
from machinekit import rtapi as rt

#from hal_tclab import hal_tclab
#from therm_unify import therm_unify
#from therm_vcp import therm_vcp

#rt.init_RTAPI()
#lab = rt.newinst("hal_tclab", "llllab")
#hal.addf("newinst","servo-thread")
#tclab= hal_tclab("hal_clab")
hal.loadusr("hal_tclab")
hal.loadusr("therm_unify")
#hal.addf(lab.name,"servo-thread")



#unify_bed= therm_unify("unify_bed")
#unify_e0= therm_unify("unify_e0")

#vcp_bed= therm_vcp("vcp_bed")
#vcp_e0= therm_vcp("vcp_e0")



#loadusr hal_tclab
#loadusr therm_unify therm_unify.0
#unify_bed= create_

#hal.loadusr('hal_tclab')

#hal.Pin('').link

#loadusr therm_unify therm_unify.1 
#load two, one for bed, one for e0

#loading therm signals, for Mcommands and gui

#bedTemp = hal.newsig("bed.temp", hal.HAL_FLOAT)
#bedsetPoint = hal.newsig("bed.setpoint", hal.HAL_FLOAT)
#bedsetPointM = hal.newsig("bed.setpointM", hal.HAL_FLOAT)
#bedsetPointGUI = hal.newsig("bed.setpointGUI", hal.HAL_FLOAT)
#newsig bed.temp float
#newsig bed.setpoint float
#newsig bed.setpointM float
#newsig bed.setpointGUI float

#newsig e0.temp float
#newsig e0.setpoint float
#newsig e0.setpointM float
#newsig e0.setpointGUI float


#net bed.setpoint => hal_tclab.setpoint-0
#net bed.setpoint <= therm_unify.0.out
#net bed.setpointM => therm_unify.0.in.0
#net bed.setpointGUI => therm_unify.0.in.1




#net e0.setpoint => hal_tclab.setpoint-1
#net e0.setpoint <= therm_unify.1.out
#net e0.setpointM => therm_unify.1.in.0
#net e0.setpointGUI => therm_unify.1.in.1
 



#connect output to tclab

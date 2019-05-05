import hal
#import hal_tclab
#import therm_unify




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

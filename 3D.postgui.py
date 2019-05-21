#!/usr/bin/python2
import hal

hal.net("ALLenable", "hal_tclab.enable")


hal.net("e0.temp", "pyvcp.E0.Temp")
hal.net("e0.temp", "hal_tclab.temperature-0")

hal.net("bed.temp", "pyvcp.Bed.Temp")
hal.net("bed.temp", "hal_tclab.temperature-1")


hal.net("bed.setpoint" , "hal_tclab.setpoint-1")
hal.net("bed.setpoint", "therm_unify.0.out")
hal.net("bed.setpointM , therm_unify.0.in.0")
hal.net("bed.setpointGUI , therm_unify.0.in.1")

hal.net("e0.setpoint", "hal_tclab.setpoint-0")
hal.net("e0.setpoint", "therm_unify.1.out")
hal.net("e0.setpointM", "therm_unify.1.in.0")
hal.net("e0.setpointGUI", "therm_unify.1.in.1")

hal.net("e0.setpoint", "pyvcp.E0.Temp.set")
hal.net("bed.setpoint", "pyvcp.Bed.Temp.set")

hal.newsig("e0.decrease", hal.HAL_BIT)
hal.newsig("e0.increase", hal.HAL_BIT)


hal.net("e0.setpoint ", "therm_vcp.e0.setpoint-in")
hal.net("e0.decrease ", "pyvcp.E0.Temp.decrease")
hal.net("e0.decrease ", "therm_vcp.e0.decrease")
hal.net("e0.increase ", "pyvcp.E0.Temp.increase")
hal.net("e0.increase ", "therm_vcp.e0.increase")
hal.net("e0.setpointGUI ", "therm_vcp.e0.setpoint-out")


hal.newsig("bed.decrease", hal.HAL_BIT)
hal.newsig("bed.increase", hal.HAL_BIT)


hal.net("bed.setpoint", "therm_vcp.bed.setpoint-in")
hal.net("bed.decrease", "pyvcp.Bed.Temp.decrease")
hal.net("bed.decrease", "therm_vcp.bed.decrease")
hal.net("bed.increase", "pyvcp.Bed.Temp.increase")
hal.net("bed.increase", "therm_vcp.bed.increase")
hal.net("bed.setpointGUI", "therm_vcp.bed.setpoint-out")

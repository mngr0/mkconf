#newsig bed.temp float
#newsig bed.setpoint float
#newsig e0.temp float
#newsig e0.setpoint float

net e0.temp <= hal_tclab.temperature-0
net e0.temp => pyvcp.E0.Temp
 
#net e0.setpoint <= hal_tclab.setpoint-0

#net e0.setpoint => pyvcp.E0.Temp.set 


net bed.temp <= hal_tclab.temperature-1
net bed.temp => pyvcp.Bed.Temp 
#net bed.setpoint => hal_tclab.setpoint-1
#net bed.setpoint => pyvcp.Bed.Temp.set 



net bed.setpoint => hal_tclab.setpoint-1
net bed.setpoint <= therm_unify.0.out
net bed.setpointM => therm_unify.0.in.0
net bed.setpointGUI => therm_unify.0.in.1

net e0.setpoint => hal_tclab.setpoint-0
net e0.setpoint <= therm_unify.1.out
net e0.setpointM => therm_unify.1.in.0
net e0.setpointGUI => therm_unify.1.in.1

net e0.setpoint => pyvcp.E0.Temp.set
net bed.setpoint => pyvcp.Bed.Temp.set

newsig e0.decrease bit
newsig e0.increase bit

net e0.setpoint => therm_vcp.e0.setpoint-in 
net e0.decrease => pyvcp.E0.Temp.decrease
net e0.decrease => therm_vcp.e0.decrease
net e0.increase => pyvcp.E0.Temp.increase
net e0.increase => therm_vcp.e0.increase
net e0.setpointGUI => therm_vcp.e0.setpoint-out 



newsig bed.decrease bit
newsig bed.increase bit

net bed.setpoint => therm_vcp.bed.setpoint-in 
net bed.decrease => pyvcp.Bed.Temp.decrease
net bed.decrease => therm_vcp.bed.decrease
net bed.increase => pyvcp.Bed.Temp.increase
net bed.increase => therm_vcp.bed.increase
net bed.setpointGUI => therm_vcp.bed.setpoint-out 

from machinekit import hal
import sys

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

print("menu:\n\t1)sali\n\t2)scendi\n\t3)salva\n")
opt=raw_input()
try:
  opt=int(opt)
except:
  print("comando non valido")
  sys.exit(0)
print("quanto:")
change=raw_input() #rimpiazzare , con .

try:
  change=float(change)
  if opt == 2:
    change=-change
except:
  print("comando non valido")
  exit(0)

for i in range(3):
  home[i].set(home[i].get()-change)
  homeoffset[i].set(homeoffset[i].get()-change)


#salvare

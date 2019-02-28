#!/usr/bin/python
import linuxcnc
import time
from subprocess import check_output


def wc(filename):
    return int(check_output(["wc", "-l", filename]).split()[0])




while 1:
	c= linuxcnc.stat()

	c.poll()
	l=c.current_line
	f=c.file
	n=wc(f)
	print "linea %s di %s, stato=%s per cento"%(str(l),str(n),(l*100/n))

time.sleep(2)

#!/bin/bash

cd /home/machinekit/Desktop/Y/bianca

rename 's/ /_/g' *
for opt in `ls *.gcode`
do

if [ $opt -nt "/home/machinekit/Desktop/ngcfiles/`basename $opt .gcode`.ngc" ]; then
	echo "new version of $opt found"
	rm "/home/machinekit/Desktop/ngcfiles/`basename $opt .gcode`.ngc"
fi

if [ ! -f "/home/machinekit/Desktop/ngcfiles/`basename $opt .gcode`.ngc" ]; then

echo "start with $opt"

cd /home/machinekit/Desktop/Y/bianca

cp "$opt" "/home/machinekit/Desktop/ngcfiles/$opt"

echo "copied locally"

cd "/home/machinekit/Desktop/ngcfiles/"


sed -i '
s/E/A/g
s/S/P/g
/^.\{80\}./ d
/^M82/ d
/^M106/ d
s/T0//' $opt
echo "gcode -> ngc"


mv "$opt" "`basename $opt .gcode`.ngc"
echo "renamed ngc"

fi

done


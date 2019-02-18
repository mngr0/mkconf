#!/bin/bash

cd /home/machinekit/Desktop/Y/delta60files

rename 's/ /_/g' *
for opt in `ls *.gcode`
do

if [ ! -f "/home/machinekit/Desktop/ngcfiles/`basename $opt .gcode`.ngc" ]; then

echo "start with $opt"

cd /home/machinekit/Desktop/Y/delta60files

cp "$opt" "/home/machinekit/Desktop/ngcfiles/$opt"

echo "copied locally"

cd "/home/machinekit/Desktop/ngcfiles/"


sed -i '
s/E/A/g
s/S/P/g
/^.\{80\}./ d
/^M82/ d
/^M106/ d' $opt
echo "gcode -> ngc"


mv "$opt" "`basename $opt .gcode`.ngc"
echo "renamed ngc"

fi

done


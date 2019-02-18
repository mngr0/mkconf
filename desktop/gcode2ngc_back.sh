#!/bin/bash

cd Y/delta60files

rename 's/ /_/g' *
for opt in `ls *.gcode`
do

if [ ! -f "/home/machinekit/Desktop/ngcfiles/`basename $opt .gcode`.ngc" ]; then

echo "start with $opt"

cp "$opt" "/home/machinekit/Desktop/ngcfiles/$opt"

echo "copied locally"

cd "/home/machinekit/Desktop/ngcfiles/"


sed -i '
s/E/A/g
' $opt




echo "E and A"

sed -i 's/S/P/g' $opt
echo "S and P"

#sed -i '/^;/ d' $opt
#echo "removed comments"

sed -i '/^.\{80\}./ d' $opt
echo "removed long comments"


sed -i '/^M82/ d' $opt
echo "removed M82"

#sed -i '/^M107/ d' $opt
#echo "removed M107"

sed -i '/^M106/ d' $opt
echo "removed M106"

#sed -i '/^M203/ d' $opt
#echo "removed M203"


mv "$opt" "`basename $opt .gcode`.ngc"
echo "renamed ngc"

fi

done


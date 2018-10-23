#!/bin/bash
cd ngcfiles

rename 's/ /_/g' *
for opt in `ls *.gcode`
do
echo "start with $opt"
sed -i 's/E/A/g' $opt
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

done


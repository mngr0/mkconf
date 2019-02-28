for i in `ls desktop`
do
 echo "$i"
  if [ ! -f ~/Desktop/$i ]; then
   ln  desktop/$i ~/Desktop/$i
  else
   echo "already existing"
  fi
 echo "done"
done

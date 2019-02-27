for i in `ls desktop`
do
echo "$i"
ln  desktop/$i ~/Desktop/$i
echo "done"
done

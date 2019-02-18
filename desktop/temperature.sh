while [ 1 ]; do
  echo -n "extruder :";
  halcmd getp Therm.ch-04.value;
  #echo -n "\n";
  echo -n "bed      :";
  halcmd getp Therm.ch-05.value;
  sleep 5;
done;

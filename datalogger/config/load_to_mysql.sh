#!/bin/bash
. /KWH/datalogger/config/datalogger.conf

count=0
for i in $(config); do
  count=$(($count+1))
  if [ $(($count%2)) -eq 1 ]; then
    sql="use datalogger; insert into config (\`key\`, \`value\`, time_created, active) values ('$i', '"
  else
    sql=$sql"$i', now(), 1);"
    echo $sql | mysql -u pi
  fi
done 

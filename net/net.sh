#!/bin/bash

# Load alias so setconf will work
source /kwh/config/kwh.conf

# Start with APN="wholesale"
setconf APN wholesale

# Start simserver.service
sudo systemctl start simserver.service

#1
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/1tcp.sh >> /kwh/log/net.log
wait

#2
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/2tcp.sh >> /kwh/log/net.log
wait

#3
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/3tcp.sh >> /kwh/log/net.log
wait

#4
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/4tcp.sh >> /kwh/log/net.log
wait

#10
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/10.sh >> /kwh/log/net.log
wait

#20
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/20.sh >> /kwh/log/net.log
wait

#30
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/30.sh >> /kwh/log/net.log
wait

#40
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/40.sh >> /kwh/log/net.log
wait

#11
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/11.sh >> /kwh/log/net.log
wait

#21
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/21.sh >> /kwh/log/net.log
wait

#31
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/31.sh >> /kwh/log/net.log
wait

#41
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/41.sh >> /kwh/log/net.log
wait

#12
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/12.sh >> /kwh/log/net.log
wait

#22
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/22.sh >> /kwh/log/net.log
wait

#32
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/32.sh >> /kwh/log/net.log
wait

#42
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/42.sh >> /kwh/log/net.log
wait

#13
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/13.sh >> /kwh/log/net.log
wait

#23
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/23.sh >> /kwh/log/net.log
wait

#33
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/33.sh >> /kwh/log/net.log
wait

#43
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/43.sh >> /kwh/log/net.log
wait

#14
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/14.sh >> /kwh/log/net.log
wait

#24
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/24.sh >> /kwh/log/net.log
wait

#34
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/34.sh >> /kwh/log/net.log
wait

#44
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/44.sh >> /kwh/log/net.log
wait

#15
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/15.sh >> /kwh/log/net.log
wait

#25
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/25.sh >> /kwh/log/net.log
wait

#35
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/35.sh >> /kwh/log/net.log
wait

#45
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/45.sh >> /kwh/log/net.log
wait

#16
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/16.sh >> /kwh/log/net.log
wait

#26
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/26.sh >> /kwh/log/net.log
wait

#36
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/36.sh >> /kwh/log/net.log
wait

#46
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/46.sh >> /kwh/log/net.log
wait

#17
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/17.sh >> /kwh/log/net.log
wait

#27
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/27.sh >> /kwh/log/net.log
wait

#37
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/37.sh >> /kwh/log/net.log
wait

#47
echo "truncate table kwh.tx_string" | mysql -u pi
wait
/kwh/net/collect.sh
wait
/kwh/net/47.sh >> /kwh/log/net.log
wait

# Stop simserver.service
sudo systemctl stop simserver.service

# sakis3g test
/bin/sakis3g

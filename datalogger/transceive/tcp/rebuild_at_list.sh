#!/bin/bash
DEBUG=1
source /KWH/datalogger/conf/datalogger.conf
if [ $DEBUG -eq "1" ]; then
	echo "AT+CMEE=2" > at_tcp_set.txt #set errors messages verbose
	echo "AT+CFUN=0" >> at_tcp_set.txt
else
	echo "AT+CFUN=0" > at_tcp_set.txt
fi
echo "AT+CFUN=1" >> at_tcp_set.txt
echo "AT+CIPMUX=?" >> at_tcp_set.txt
echo "AT+CIPMUX?" >> at_tcp_set.txt
echo "AT+CIPMUX=1" >> at_tcp_set.txt
echo "AT+CIPMUX=0" >> at_tcp_set.txt
echo "AT+CGATT=0" >> at_tcp_set.txt
echo "AT+CGATT=1" >> at_tcp_set.txt
#echo "AT+CIPSHUT" >> at_tcp_set.txt
echo "AT+CSTT=\"$APN\"" >> at_tcp_set.txt
#echo 'AT+CDGCONT=1,\"IP\",\"$APN\"' >> at_tcp_set.txt
echo "AT+CIICR" >> at_tcp_set.txt
echo "AT+CIFSR" >> at_tcp_set.txt
echo "AT+CIPSTART=\"TCP\",\"$DOMAIN\",\"$PORT\"" >> at_tcp_set.txt
echo "AT+CIPSEND" >> at_tcp_set.txt
#head -c 100 /datalogger/transceive/tcp/tstring > /dev/ttyAMA0 ;
echo $'\cZ' >> at_tcp_set.txt
echo "AT+CIPCLOSE" >> at_tcp_set.txt
echo "AT+CIPSHUT" >> at_tcp_set.txt

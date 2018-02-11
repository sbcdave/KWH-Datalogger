W1DIR="/sys/bus/w1/devices"

#exit if no one wire sensor exists   if [ ! -d $W1DIR ]    then    echo "There is no sensors!"exit 1    fi
DEVICES=$(ls $W1DIR)

#Output sting
OUTPUT=""

#cycle across all founded sensors
for DEVICE in $DEVICES
do
#ignor master
if [ $DEVICE != "w1_bus_master1" ]
then
    #read sensor
    ANSWER=$(cat $W1DIR/$DEVICE/w1_slave)

    #Check answer and CRC; because if sensor disapear its address will be  9x00 but CRC will be valid
    echo -e "$ANSWER" | grep -e "00 00 00 00 00 00 00 00 00"  >&2
    if [ $? -ne 0 ]
    then
        #Temp is valid if CRC is valid
	echo -e "$ANSWER" | grep -q "YES"  >&2
	if [ $? -eq 0 ]
	then
	    #temp is OK
	    #Get only temp from two line answer
	    TEMP=$(echo -e "$ANSWER" | grep "t=" | cut -f 2 -d "=")

	    INTEGER=$(($TEMP/1000)) #integers
	    FRAC=$(($TEMP%1000)) #decimals

	    #handle minus frac! int (-1,0)°C
	    if [ "$FRAC" -lt "0" ] #is rest minus?
            then
     	        FRAC=$(($FRAC * -1)) #del minus
	        if [ "$INTEGER" -ge "0" ] #is INTEGER 0 and more?
	        then
         	    INTEGER="-0" #this write minus to result, zero will be add next
	        fi
	    fi
	    #Handle one or two cyfer result - int (-1, 1)°C
	    if [ "$FRAC" -lt "100" ] #is result less than  100?
	    then
	        if [ "$FRAC" -lt "10" ] #is result less than 10?
	        then
	            FRAC="00"$FRAC #add two zeros
	        else
	            FRAC="0"$FRAC #add one zero
	        fi
	    fi

	    echo -n "$INTEGER.$FRAC" > /KWH/datalogger/temp/$DEVICE
        else
	#CRC is invalid - error
	    echo "$DEVICE=CRC ERROR" >&2

   	fi
    fi
fi
done

